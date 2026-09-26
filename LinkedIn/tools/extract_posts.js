/* extract_posts.js — page-eval helper for the LinkedIn activity feed.
 *
 * Run inside the live browser task on
 *   https://www.linkedin.com/in/<handle>/recent-activity/all/
 * AFTER scrolling to the bottom until no new posts load.
 *
 * Returns an array of post stubs:
 *   [{activity_id, url, text, posted_at, likes, comments, reposts,
 *     post_type, shared_article}]
 *
 * Selectors target LinkedIn's 2026 DOM; if LinkedIn changes markup, adapt the
 * queries but keep the output shape — build.py depends on it.
 */
(() => {
  const out = [];
  const seen = new Set();

  // Every post card links to its canonical /posts/ URL containing "activity-<id>".
  const links = document.querySelectorAll('a[href*="/posts/"][href*="activity-"]');
  for (const a of links) {
    const href = a.href.split('?')[0];
    const m = href.match(/activity-(\d+)/);
    if (!m || seen.has(m[1])) continue;
    seen.add(m[1]);

    // Walk up to the post card container.
    const card = a.closest('div.feed-shared-update-v2')
      || a.closest('li.artdeco-list__item')
      || a.closest('div[data-urn]')
      || a.parentElement;

    const textEl = card && card.querySelector(
      'div.feed-shared-update-v2__description, div.update-components-text, span.break-words'
    );
    const text = textEl ? textEl.innerText.trim() : '';

    // Timestamp: LinkedIn renders relative ("2d") or absolute in <time>.
    let posted_at = null;
    const timeEl = card && card.querySelector('time[datetime]');
    if (timeEl) posted_at = timeEl.getAttribute('datetime');

    const num = (re) => {
      const el = card && [...card.querySelectorAll('span,button')].find(e => re.test(e.textContent || ''));
      if (!el) return 0;
      const n = (el.textContent.match(/[\d,]+/) || ['0'])[0].replace(/,/g, '');
      return parseInt(n, 10) || 0;
    };

    // Article share detection: card links to /pulse/ or an external article card.
    let shared_article = null;
    const artLink = card && card.querySelector('a[href*="/pulse/"]');
    if (artLink) {
      shared_article = { title: artLink.innerText.trim() || null, url: artLink.href.split('?')[0] };
    }

    out.push({
      activity_id: m[1],
      url: href,
      text,
      posted_at,
      likes: num(/like/i),
      comments: num(/comment/i),
      reposts: num(/repost/i),
      post_type: shared_article ? 'article_share' : 'original',
      shared_article,
    });
  }
  return out;
})();
