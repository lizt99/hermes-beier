---
name: creative-content-and-design
description: "Use when creating complex narrative content, social media strategies, UI/UX designs, or generating project ideas. This umbrella skill provides frameworks for: (1) Novel writing and world-building (Novel Architect), (2) Social media research and content strategy (Social Media Ops), (3) UI/UX design intelligence and implementation (UI/UX Pro Max), and (4) Constraint-driven project generation (Creative Ideation)."
---

# Creative Content and Design

This skill consolidates specialized workflows for creative output, from storytelling to interface design.

## 1. Narrative & World-Building (Novel Architect)
**Trigger**: When writing a novel, creating a story world, or managing complex narrative projects.
- **Mindset**: Maintain a consistent "truth state" (world, characters, subplots) using JSON files.
- **Workflow**: Triage (Genre/Concept) → Initialize Workspace (`books/<id>/story/`) → Iterative Pipeline:
  1. **Planning**: Scene goals and hooks.
  2. **Composition**: "Show, Don't Tell" prose (~3000 words).
  3. **State Settlement**: Extract new facts and update JSON truth files.
  4. **Audit**: 33-dimensions of quality check.
- **Truth Files**: `world_state.json`, `character_matrix.json`, `subplot_board.json`.

## 2. Social Media Operations
**Trigger**: Research, content creation, and automation for platforms like Xiaohongshu (XHS) or TikTok.
- **Research**: Use indirect search (`site:domain.com "query"`) to bypass login walls/captchas.
- **Persona**: Use a "Neighbor Sister" tone—warm, helpful, and sincere.
- **Format**: High-engagement notes with emojis and "savable" information.
- **Visuals**: Use infographics to hooks users.

## 3. UI/UX Design Intelligence
**Trigger**: When building polished interfaces, design systems, or UX flows.
- **Triage**: Platform, Stack (Tailwind/React/etc.), Brand Vibe, Accessibility.
- **Deliverables**: UI Layouts, UX Journey Maps, Design System Tokens, Implementation Plans.
- **Standards**: ASCII tokens by default, cover all states (loading/error/empty), keyboard nav, and contrast.

## 4. Creative Ideation
**Trigger**: When the user asks for project ideas, inspiration, or "what should I build?"
- **Action**: Use creative constraints to generate 3 concrete project ideas.
- **Rule**: Interpret constraints broadly (text-as-geometry, hostile UI, Frankenstein week).
- **Reference**: `references/ideation.md` for the full prompt library.

## 5. Visual Arts & Media (ComfyUI, p5.js, Manim)
- **Generative Art**: Use `p5js` for interactive/generative sketches and `comfyui` for stable diffusion workflows.
- **Animations**: Use `manim-video` for mathematical and algorithmic animations.
- **Diagramming**: Use `architecture-diagram` and `excalidraw` for technical and hand-drawn visuals.
- **ASCII Creativity**: Use `ascii-art`, `ascii-video`, and `pretext` for text-based visual demos.

## Sub-Workflows (References)
- `references/novel-architect.md`: Detailed multi-agent pipeline and audit criteria.
- `references/social-media.md`: XHS research patterns and content templates.
- `references/ui-ux.md`: Design system rules and component guidelines.
- `references/ideation.md`: Full constraint library for project generation.
