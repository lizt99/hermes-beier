# Xiaohongshu (XHS) Research & Bot Avoidance

## Effective Search Patterns

Because Xiaohongshu (XHS) has aggressive bot detection on its web search, use external search engine indexing for stable research.

### 1. Google/Bing Dorking
Use the following pattern in `browser_navigate` or `web_search`:
`site:xiaohongshu.com "keyword" OR "topic"`

### 2. Identifying High-Value Content
When reviewing search results, look for these markers in titles/snippets:
- **"干货" (Gān Huò)**: Valuable, practical info.
- **"整理" (Zhěng Lǐ)**: Curated lists or collections.
- **"避雷" (Bì Léi)**: Things to avoid (high engagement).
- **"懒人版" (Lǎn Rén Bǎn)**: Simplified/cheat sheet versions.

## Technical Workarounds

### Browser Sandbox Fix
If `browser_navigate` fails with `No usable sandbox!` on a server/Docker:
- **Action**: Add `--no-sandbox` to the browser arguments.
- **Config**: Set `AGENT_BROWSER_ARGS="--no-sandbox,--disable-gpu"` in the profile's `.env` file.

### Dealing with Login Walls
XHS web platform limits scrolling for unauthenticated users. 
- **Workaround**: Extract the `url` from search results and use `web_extract` or `browser_navigate` for individual page reads, which are less likely to trigger a wall than continuous search-result scrolling.

## Persona: "Neighbor Sister" (邻家妹妹)
- **Opening**: "姐妹们！" (Sisters!) or "最近发现个宝藏..." (Recently found a treasure...)
- **Core**: Share personal experience, not just facts.
- **Visuals**: Mention things like "原图无滤镜" (original pic, no filter) to build trust.
- **Closing**: "大家还有什么想看的嘛？" (What else do you guys want to see?)
