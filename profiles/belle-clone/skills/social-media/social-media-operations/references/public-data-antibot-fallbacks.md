# Public Data Anti-Bot Fallbacks

## Session pattern: lottery/public-results lookup

Observed working sequence for publicly visible structured data that is inconsistently protected:

1. Try official/public source with `terminal` or `requests`.
2. If the site returns anti-bot HTML/403, do not assume the data is inaccessible.
3. Open the human-readable page with `browser_navigate`.
4. Extract values directly from the browser snapshot when the page visibly renders the target table.
5. Only reverse-engineer hidden JSON/API endpoints if that is materially necessary.

## Concrete example

### Blocked path
- `https://www.cwl.gov.cn/ygkj/wqkjgg/3d/` returned 403 anti-bot HTML in terminal requests.
- DuckDuckGo/Baidu/Bing search attempts were low-signal or captcha-prone for this query.

### Working path
- `https://www.zhcw.com/kjxx/3d/` rendered in the browser tool.
- The snapshot exposed the historical table directly, including rows such as:
  - `2026114` → `2026-05-04` → `8 6 4`
  - `2026113` → `2026-05-03` → `0 4 0`
  - `2026112` → `2026-05-02` → `0 6 5`

## JS-endpoint reconnaissance pattern

Useful clues can often be found in page JS without full browser automation:
- Config vars like `urlYm`, `urlDz`
- Static assets like `/chartstatic/json/...`
- RPC hints like `transactionType=10001001`

In this session:
- `https://www.zhcw.com/static/js/kjsj.min.js` exposed lottery IDs and endpoint hints.
- `https://www.zhcw.com/chartstatic/json/kj_3d.json` existed but only contained old static data, so it was not reliable for current results.
- `https://jc.zhcw.com/port/client_json.php` accepted requests but returned blank content from terminal, making browser snapshot extraction the faster reliable fallback.

## Decision rule

Prefer the browser snapshot when all of these are true:
- the page visibly renders the needed rows,
- the source is clearly identifiable,
- hidden APIs are blocked/blank/undocumented,
- and the user only needs the displayed facts rather than a reusable scraper.
