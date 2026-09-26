/* extract_comments.js — page-eval helper for a single LinkedIn post page.
 *
 * Run inside the live browser task on the post's canonical URL.
 * Phase 1 (expand): clicks every "Load more comments" / "View N replies"
 *   button until none remain (bounded loop with pauses for lazy loading).
 * Phase 2 (serialize): walks the comment tree and returns:
 *   {comments: [{comment_id, author:{name, profile_url, headline},
 *                is_author_reply, posted_at, text, likes, replies:[...]}]}
 *
 * `ownerProfileUrl` must be passed in (the archive owner's /in/<handle> URL);
 * comments whose author link matches it get is_author_reply = true.
 * Adapt selectors to the live DOM if LinkedIn changes markup, but keep the
 * output shape — build.py depends on it.
 */
async function extractLinkedInComments(ownerProfileUrl) {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const norm = (u) => (u || '').split('?')[0].replace(/\/$/, '');

  // ---- Phase 1: expand everything ----
  for (let round = 0; round < 25; round++) {
    const btns = [...document.querySelectorAll('button')].filter((b) => {
      const t = (b.textContent || '').trim().toLowerCase();
      return /load more comments|previous comments|view .* repl|show .* repl|more replies/.test(t)
        && b.offsetParent !== null;
    });
    if (btns.length === 0) break;
    for (const b of btns) { try { b.click(); } catch (e) {} }
    await sleep(1800);
    // Scroll the comments region to trigger lazy rendering.
    const region = document.querySelector('section.comments, div.comments-comments-list')
      || document.scrollingElement;
    if (region && region.scrollTo) region.scrollTo({ top: region.scrollHeight });
    await sleep(800);
  }

  // ---- Phase 2: serialize ----
  const parseComment = (node, depth) => {
    const authorA = node.querySelector('a[href*="/in/"]');
    const profile_url = authorA ? norm(authorA.href) : null;
    const nameEl = node.querySelector('span.comments-post-meta__name, span[class*="commenter-name"]')
      || (authorA && authorA.querySelector('span'));
    const headlineEl = node.querySelector('span.comments-post-meta__headline, div[class*="commenter-headline"]');
    const textEl = node.querySelector('div.comments-comment-item__main-content, div[class*="comment-text"], span[class*="comment-body"]');
    const timeEl = node.querySelector('time[datetime]');
    const likeBtn = [...node.querySelectorAll('button')].find((b) => /like/i.test(b.getAttribute('aria-label') || ''));
    let likes = 0;
    if (likeBtn) {
      const mm = (likeBtn.getAttribute('aria-label') || '').match(/[\d,]+/);
      if (mm) likes = parseInt(mm[0].replace(/,/g, ''), 10);
    }
    const c = {
      comment_id: node.getAttribute('data-id') || node.getAttribute('data-urn') || null,
      author: {
        name: nameEl ? nameEl.innerText.trim() : (authorA ? authorA.innerText.trim() : null),
        profile_url,
        headline: headlineEl ? headlineEl.innerText.trim() : null,
      },
      is_author_reply: !!profile_url && norm(ownerProfileUrl) === profile_url,
      posted_at: timeEl ? timeEl.getAttribute('datetime') : null,
      text: textEl ? textEl.innerText.trim() : '',
      likes,
      replies: [],
    };
    if (depth < 1) {
      // Nested replies live in a replies container inside the comment node.
      const replyNodes = node.querySelectorAll(
        ':scope div.comments-comment-item--nested, :scope ul.comments-replies-list > li, :scope div[class*="reply-item"]'
      );
      replyNodes.forEach((r) => {
        if (r !== node) c.replies.push(parseComment(r, depth + 1));
      });
    }
    return c;
  };

  const roots = document.querySelectorAll(
    'section.comments li.comments-comment-item:not(.comments-comment-item--nested), ' +
    'div.comments-comments-list > div.comments-comment-item, ' +
    'article[class*="comment"]:not([class*="reply"])'
  );
  const comments = [];
  roots.forEach((n) => {
    // Skip nodes that are themselves nested replies of another captured node.
    if (n.closest('.comments-replies-list, div[class*="replies-container"]') && n.matches('.comments-comment-item--nested')) return;
    comments.push(parseComment(n, 0));
  });
  return { comments };
}

// The browser task calls:  await extractLinkedInComments("https://www.linkedin.com/in/<handle>")
