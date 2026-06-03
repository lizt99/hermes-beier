# Xiaohongshu (XHS) Technical Notes

## Scraping & Research Challenges

### 1. Browser Sandbox Issues
In restricted environments (Docker, VMs), `browser_navigate` may fail with:
`FATAL:zygote_host_impl_linux.cc:128] No usable sandbox!`
**Fix**: Add `--no-sandbox` to browser arguments in `config.yaml`.

### 2. Dependency Limitations
Standard sandboxes for `execute_code` often lack `beautifulsoup4` or `requests`. 
**Workaround**: Use `urllib.request` and `re` (Standard Library only) for simple HTTP fetches.

### 3. Search Engine Indexing
XHS content is often best accessed via external search engines using `site:xiaohongshu.com`. Direct searches on the XHS web platform frequently trigger login walls or captchas.

### 4. Search Block Cascade
In high-security environments, you may hit a "Block Cascade" where Google, Bing, Baidu, and DuckDuckGo all present captchas for the same query. 
**Strategy**: When this happens, stop trying search engines. Pivot to Bilibili or YouTube search. These platforms are often less aggressive toward bot signatures and contain expert "Methodology" videos that extract XHS trends for you.

## Robust Search Pattern (Python StdLib)

### 4. Keyword Sensitivity (Financial/Debt Niche)
XHS is highly sensitive to financial "grey area" terms. 
- **Banned/High-Risk**: 停息挂账 (Stop-interest), 债务重组 (Debt restructuring), 停催 (Stop collection), 话术 (Script).
- **Safe Alternatives**: 延期分期 (Extension/Installment), 自救计划 (Self-rescue plan), 心理重建 (Psychological reconstruction), 经验分享 (Experience sharing).
- **Visual Safety**: Use real-life photos (handwritten notes, redacted screenshots) to avoid being flagged as a "template-based bot" or "fake agency."
