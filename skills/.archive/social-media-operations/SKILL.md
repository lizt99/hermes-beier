---
name: social-media-operations
description: "Research, content creation, and automation for social media platforms (Xiaohongshu, TikTok, etc.)."
version: 1.1.0
author: Belle
metadata:
  hermes:
    tags: [social-media, xhs, xiaohongshu, marketing, content-creation, scraping, research]
    related_skills: [xurl, baoyu-infographic, creative]
---

# Social Media Operations

This skill covers strategies, research techniques, and content automation for visual and trend-driven social media platforms, with a primary focus on **Xiaohongshu (小红书)**.

## Core Workflows

### 1. Platform Research & Trend Analysis
Social platforms are highly sensitive to automation.
- **Search Strategy**: Avoid direct站内 (in-app) search when unauthenticated. Use `site:<domain> <query>` on search engines (Google, Bing) to find indexed content and bypass login walls/captchas.
- **Indirect Search Pattern**: When searching for trends or specific user content without an API/logged-in session:
  ```
  # Google search pattern
  site:xiaohongshu.com "爆款" 2024
  ```
- **Competitive Analysis**: Focus on "Keywords" (关键词), "Tags" (标签), and "Cover Image Layout" (封面图布局).
- **Pitfall**: Direct `requests` or `curl` calls often trigger challenge pages. Use `browser_navigate` with a real User-Agent and `--no-sandbox` if in a restricted environment.

### 2. Content Strategy: The "Neighbor Sister" Persona
For organic engagement, use a relatable, friendly persona:
- **Tone**: Warm, helpful, and sincere. Avoid corporate or overly clinical language.
- **Format**: Use lists, bullet points, and emojis (😊, ✨, 💖).
- **Engagement**: Focus on providing emotional value and "savable" (值得收藏) information.

### 3. Visual Content Creation
- **Information Design**: Use `baoyu-infographic` to turn text data into shareable visual "notes".
- **Visual Hooks**: Design covers that highlight a single strong problem or transformation.

## References
- `references/xhs-research.md`: Detailed search patterns and bot-avoidance recipes.
- `templates/xhs-post.md`: Structure for high-engagement notes.

## Related Skills
- `xurl`: Operations for X/Twitter.
- `baoyu-infographic`: Infographics for social media.
- `creative`: Aesthetic design and ASCII art.
