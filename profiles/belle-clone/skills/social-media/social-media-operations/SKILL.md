---
name: social-media-operations
description: "Research, content creation, and automation for social media platforms (Xiaohongshu, TikTok, etc.)."
version: 1.0.0
author: Belle
metadata:
  hermes:
    tags: [social-media, xhs, xiaohongshu, marketing, content-creation, scraping]
    related_skills: [xurl, baoyu-infographic, creative]
---

# Social Media Operations

This skill covers strategies, research techniques, and automation workflows for major social media platforms, with a focus on visual and content-driven platforms like **Xiaohongshu (小红书)**.

> **Scope Boundary:** This skill acts as a general-purpose operational command center for social media and private-domain workflows. Do NOT embed project-specific SOPs, runbooks, or context (e.g., "Project Shang-An") directly into this skill. Project-specific execution guides should live in their respective project directories or dedicated archived skills.

## Core Workflows

### 1. Xiaohongshu (XHS) Research
Xiaohongshu is highly sensitive to bots and JS-heavy. 
- **Search Strategy**: Use `site:xiaohongshu.com` on Google/Bing rather than direct scraping if a browser isn't available.
- **Content Analysis**: Focus on "Keywords" (关键词), "Tags" (标签), and "Cover Image Layout" (封面图布局).
- **Pitfall**: Direct `requests` calls often return empty or challenge pages. Use the `browser_navigate` tool with a real user-agent.

### 2. Research Intent vs. Meta-Analysis
- **Intent Correction**: When a user asks to "research topic X on platform Y", prioritize finding raw content *from* platform Y (using `site:Y.com X`) over meta-analysis *about* topic X on platform Y (searching for "X on platform Y" on tech news sites).
- **Secondary Source Fallback**: If platform Y is heavily blocked (captchas, login walls), use Video (Bilibili/YouTube) or Q&A (Zhihu) platforms. Search for `[Platform Name] + [Topic] + [Strategy/Case Study]` to find expert teardowns which often contain the raw content insights you're missing.

### 3. Strategy & Risk Management
- **Reverse Verification**: Always perform "negative research" to find failure cases, account bans, and user pet peeves for a specific niche. 
- **Compliance & Euphemisms**: Use compliant alternatives for sensitive keywords (e.g., in the debt niche, use "延期分期" instead of "停息挂账").
- **Persona Alignment**: Align the visual style (Hardcore vs. Emotional) with the core value pillar selected.

## Troubleshooting & Bot Detection

### 1. Browser "No Usable Sandbox"
- Run the browser with `--no-sandbox` if running in a containerized environment.

### 2. Search Engine Captchas
- **Aggressive Blocking**: If Google, Bing, Baidu, and DuckDuckGo all fail (as seen in high-security sessions), pivot immediately to **Secondary Sources** (Bilibili/YouTube/Zhihu) rather than trying more search engines.
- **Headless Fallback**: Use `terminal` + `curl -A "Mozilla/5.0" <search_url> | grep -oP '...'` to extract links/titles if the full browser is blocked.

### 3. Official Site Anti-Bot + Browser Snapshot Fallback
When an official results site blocks `requests`/`curl` with 403 or anti-bot pages, but the browser tool can still render the page:
- Open the human-facing results page with `browser_navigate`.
- Read the visible table from the browser snapshot instead of insisting on the JSON/API path.
- Treat browser-extracted values as grounded if the snapshot clearly shows the rows.

### 4. Lightweight Public-Data Discovery via Page JS
For JS-heavy sites with hidden data endpoints:
- Fetch the page HTML with `terminal`/`requests`.
- Inspect referenced JS files for config variables and endpoint hints.
- Try static JSON assets before reverse-engineering dynamic endpoints.
- If the documented API responds blank or blocked, fall back to browser-rendered page data rather than over-investing in the hidden API.

## Private-Domain Community Operations Umbrella
Use this umbrella section when the work is not just public-platform content research/publishing, but the downstream operating system that converts public traffic into structured private-domain communities, trust loops, intake, and compliant service routing.

### A. Shared operating model
Treat the system as a coordinated funnel rather than ad hoc chatting:
- public platform content acquires attention
- entry assets and hooks convert attention into contact/join actions
- community or private-domain spaces establish trust and order
- operators tag, segment, and route members by need
- deeper consultation or service happens with explicit scope boundaries

### B. Default command posture
When this subsection applies, Belle should behave as an operations commander:
- diagnose current stage and bottlenecks
- define the next execution round
- assign role-specific tasks that humans can directly perform
- request structured feedback instead of free-form updates
- review results using scale / hold / optimize / stop logic

### C. Output shapes for community/private-domain work
Default deliverables may include:
- onboarding SOP
- moderation rules
- task assignments by role
- need-tagging framework
- daily or weekly command cards
- review dashboards and next-step memos

### D. WeChat debt-support subgroup operations
The specific WeChat debt-support group operating system belongs under this umbrella. Use:
- `references/wechat-debt-support-group-ops.md` for the full domain-specific SOP
- `templates/wechat-7-day-rhythm.md`
- `templates/wechat-daily-command-card.md`
- `templates/wechat-team-feedback-card.md`

### E. YouJia Caregiver (优加陪护) Social Ops Engine
The YouJia Caregiver social media lead-generation and conversion engine (focusing on Xiaohongshu and WeChat private domain). Use:
- `references/youjia-caregiver-social-ops.md` for the core conversion flywheel and data-driven review logic
- `references/youjia-brand-guidelines.md` and `references/target-audience-analysis.md` for persona/brand context
- `templates/content-generation-card.md` for generating Xiaohongshu posts
- `templates/data-review-card.md` for diagnosing post performance

## References & Tools
- `references/public-data-antibot-fallbacks.md`: Notes on anti-bot official sites, JS endpoint discovery, and browser snapshot fallback patterns.
- `references/xhs-technical-notes.md`: Technical hurdles and workarounds for XHS data.
- `references/social-media-skills-inventory.md`: A living list of social media related tools and skills.
- `templates/xhs-post-template.md`: Structure for a high-engagement XHS note.

## Related Skills
- `xurl`: Operations for X/Twitter.
- `baoyu-infographic`: Educational social media graphics.
- `creative`: General design and ASCII art.