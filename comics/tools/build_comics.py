#!/usr/bin/env python3
"""Build comics/index.html from comics/comics.json.

The viewer is a single self-contained page in the xkcd style:
one comic at a time, |< < Prev / Random / Next > >| navigation above
and below the image, hash permalinks (#12), arrow-key navigation,
and a full archive list at the bottom. Data is embedded in the page
so it works from file:// as well as from GitHub Pages.

To add a comic: drop the image into comics/images/, append an entry
to comics/comics.json (num = previous + 1), rerun this script.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent  # comics/

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Comics — AI Management</title>
<meta name="description" content="Comics and cartoons by Horace Chan, originally posted on LinkedIn.">
<script>
(function () {
  try {
    var t = localStorage.getItem('aimgmt-theme');
    if (t !== 'dark' && t !== 'light') {
      t = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    document.documentElement.dataset.theme = t;
  } catch (e) {}
})();
</script>
<style>
  :root {
    color-scheme: light;
    --bg: #ffffff;
    --text: #1a1a1a;
    --muted: #6b6b6b;
    --line: #d8d8d8;
    --btn-bg: #f4f4f4;
    --btn-hover: #e7e7e7;
    --link: #0b5394;
    --panel: #fafafa;
  }
  html[data-theme="dark"] {
    color-scheme: dark;
    --bg: #16181d;
    --text: #e8e6e1;
    --muted: #9a958c;
    --line: #3a3d44;
    --btn-bg: #22252b;
    --btn-hover: #2c3038;
    --link: #7db3e8;
    --panel: #1d2026;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; background: var(--bg); color: var(--text);
    font-family: "Lucida Grande", "Lucida Sans Unicode", "Lucida Sans", system-ui, sans-serif;
    -webkit-font-smoothing: antialiased;
  }
  .wrap { max-width: 920px; margin: 0 auto; padding: 18px 16px 60px; text-align: center; }
  .topbar { display: flex; justify-content: space-between; align-items: baseline; font-size: 13px; margin-bottom: 6px; }
  .topbar a { color: var(--link); text-decoration: none; }
  .topbar a:hover { text-decoration: underline; }
  h1.site { font-size: 30px; margin: 10px 0 2px; letter-spacing: .5px; }
  .tagline { color: var(--muted); font-size: 13.5px; margin-bottom: 14px; }
  .comicnum { color: var(--muted); font-size: 13px; margin-top: 18px; }
  h2.title { font-size: 24px; margin: 2px 0 4px; line-height: 1.25; }
  .date { color: var(--muted); font-size: 13.5px; margin-bottom: 12px; }
  ul.nav { list-style: none; margin: 10px 0; padding: 0; }
  ul.nav li { display: inline-block; margin: 0 2px; }
  ul.nav a {
    display: inline-block; min-width: 74px; padding: 5px 10px;
    border: 1.5px solid var(--text); border-radius: 3px;
    background: var(--btn-bg); color: var(--text);
    font-size: 15px; font-weight: 600; text-decoration: none;
  }
  ul.nav a:hover { background: var(--btn-hover); }
  ul.nav a.disabled { opacity: .32; pointer-events: none; }
  .stage { margin: 8px 0 4px; }
  .stage img { max-width: 100%; height: auto; }
  .missing {
    border: 1.5px dashed var(--line); border-radius: 6px; background: var(--panel);
    padding: 56px 20px; color: var(--muted); font-size: 15px;
  }
  .missing a { color: var(--link); }
  .caption {
    max-width: 640px; margin: 14px auto 0; text-align: left;
    font-size: 15px; line-height: 1.55; white-space: pre-wrap; word-wrap: break-word;
  }
  .perma { margin-top: 16px; font-size: 13px; color: var(--muted); }
  .perma a { color: var(--link); text-decoration: none; }
  .perma a:hover { text-decoration: underline; }
  .archive { margin-top: 46px; border-top: 1px solid var(--line); padding-top: 18px; text-align: left; }
  .archive h3 { text-align: center; font-size: 17px; margin: 0 0 12px; }
  .archive ol { max-width: 640px; margin: 0 auto; padding-left: 26px; font-size: 14px; line-height: 1.9; }
  .archive a { color: var(--link); text-decoration: none; }
  .archive a:hover { text-decoration: underline; }
  .archive .ad { color: var(--muted); font-size: 12.5px; }
  footer { margin-top: 40px; color: var(--muted); font-size: 12.5px; }
  footer a { color: var(--link); text-decoration: none; }
</style>
</head>
<body>
<div class="wrap">
  <div class="topbar">
    <a href="../">&larr; AI Management</a>
    <a href="../LinkedIn/">LinkedIn posts archive</a>
  </div>

  <h1 class="site">COMICS</h1>
  <div class="tagline">Comics &amp; cartoons by Horace Chan, originally posted on <a href="https://www.linkedin.com/in/horacechan" style="color:var(--link)">LinkedIn</a>.</div>

  <ul class="nav" id="navTop"></ul>

  <div class="comicnum" id="comicNum"></div>
  <h2 class="title" id="comicTitle"></h2>
  <div class="date" id="comicDate"></div>

  <div class="stage" id="stage"></div>
  <div class="caption" id="caption"></div>

  <ul class="nav" id="navBottom"></ul>

  <div class="perma" id="perma"></div>

  <div class="archive">
    <h3>Archive</h3>
    <ol id="archiveList"></ol>
  </div>

  <footer>
    Permanent link format: this page&rsquo;s URL plus <b>#</b> and the comic number (e.g. <b>#1</b>).<br>
    Use the &larr; and &rarr; arrow keys to flip through comics.
  </footer>
</div>

<script>
var COMICS = /*__DATA__*/[];

(function () {
  var total = COMICS.length;
  var byNum = {};
  COMICS.forEach(function (c) { byNum[c.num] = c; });

  function navHTML(cur) {
    function btn(label, target, disabled) {
      return '<li><a href="#' + target + '"' + (disabled ? ' class="disabled"' : '') + '>' + label + '</a></li>';
    }
    var prev = Math.max(1, cur - 1), next = Math.min(total, cur + 1);
    return btn('|&lt;', 1, cur <= 1) +
           btn('&lt; Prev', prev, cur <= 1) +
           '<li><a href="#" id="randBtn">Random</a></li>' +
           btn('Next &gt;', next, cur >= total) +
           btn('&gt;|', total, cur >= total);
  }

  function render(num) {
    var c = byNum[num];
    if (!c) { num = total; c = byNum[num]; }
    document.title = c.title + ' — Comics';
    document.getElementById('comicNum').textContent = 'Comic #' + c.num + ' of ' + total;
    document.getElementById('comicTitle').textContent = c.title;
    document.getElementById('comicDate').textContent = c.date_display;
    var stage = document.getElementById('stage');
    if (c.image) {
      stage.innerHTML = '';
      var img = document.createElement('img');
      img.src = 'images/' + c.image;
      img.alt = c.title;
      img.title = c.title;
      stage.appendChild(img);
    } else {
      stage.innerHTML = '<div class="missing">This comic&rsquo;s image is still being recovered from LinkedIn.<br>' +
        '<a href="' + c.linkedin_url + '" target="_blank" rel="noopener">View it on LinkedIn &rarr;</a></div>';
    }
    document.getElementById('caption').textContent = c.caption;
    document.getElementById('navTop').innerHTML = navHTML(num);
    document.getElementById('navBottom').innerHTML = navHTML(num);
    document.getElementById('perma').innerHTML =
      'Permanent link to this comic: <a href="#' + c.num + '">' + location.pathname + '#' + c.num + '</a>' +
      ' &middot; <a href="' + c.linkedin_url + '" target="_blank" rel="noopener">Original post on LinkedIn</a>';
    var rb = document.querySelectorAll('#randBtn');
    rb.forEach(function (b) {
      b.addEventListener('click', function (e) {
        e.preventDefault();
        var r = num;
        while (total > 1 && r === num) r = 1 + Math.floor(Math.random() * total);
        location.hash = '#' + r;
      });
    });
    window.scrollTo(0, 0);
  }

  function currentFromHash() {
    var m = /^#(\d+)$/.exec(location.hash || '');
    return m ? parseInt(m[1], 10) : total;
  }

  var list = document.getElementById('archiveList');
  list.innerHTML = COMICS.slice().reverse().map(function (c) {
    return '<li value="' + c.num + '"><a href="#' + c.num + '">' + c.title.replace(/</g, '&lt;') + '</a> ' +
           '<span class="ad">' + c.date_display + '</span></li>';
  }).join('');

  window.addEventListener('hashchange', function () { render(currentFromHash()); });
  document.addEventListener('keydown', function (e) {
    var cur = currentFromHash();
    if (e.key === 'ArrowLeft' && cur > 1) location.hash = '#' + (cur - 1);
    else if (e.key === 'ArrowRight' && cur < total) location.hash = '#' + (cur + 1);
  });
  render(currentFromHash());
})();
</script>
</body>
</html>
"""


def main() -> None:
    data = json.loads((ROOT / "comics.json").read_text(encoding="utf-8"))
    html = TEMPLATE.replace("/*__DATA__*/", json.dumps(data, ensure_ascii=False))
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"Wrote comics/index.html with {len(data)} comics "
          f"({sum(1 for c in data if c['image'])} with images).")


if __name__ == "__main__":
    main()
