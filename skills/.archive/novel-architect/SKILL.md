---
name: novel-architect
description: "Autonomous novel writing and world-building system based on the InkOS multi-agent pipeline. Use for (1) Planning story arcs and chapter intent, (2) Generating high-quality prose with consistent world-state, (3) Auditing chapters for logic, pacing, and hooks, (4) Maintaining long-term coherence via JSON truth files (world, characters, subplots). Use when the user asks to write a novel, create a story world, or manage a complex narrative project."
---

# Novel Architect (Native OpenClaw Implementation)

This skill provides a structured multi-agent pipeline for writing high-quality fiction without delegating to external tools. It maintains a consistent "truth state" across chapters to ensure long-term narrative coherence.

## 1) Triage & Initialization
Ask only what you must to avoid wrong work:
- **Genre**: (e.g., Xuanhuan, Xianxia, Urban, LitRPG, Sci-Fi)
- **Language**: (Default: Chinese/zh)
- **Core Concept**: (The "hook" or brief)

**Setup the workspace**:
Create the following structure in your current project directory:
```
books/<book-id>/
├── story/
│   ├── state/
│   │   ├── world_state.json
│   │   ├── character_matrix.json
│   │   ├── subplot_board.json
│   │   ├── chapter_summaries.json
│   │   └── pending_hooks.json
│   ├── author_intent.md
│   ├── current_focus.md
│   └── chapters/
```

Initialize the JSON files as empty objects `{}` or arrays `[]` if starting fresh.

## 2) The Writing Pipeline (Iterative)

Follow these steps for each chapter:

### Step 1: Planning (The Planner)
Read `author_intent.md`, `current_focus.md`, and the last 3 entries in `chapter_summaries.json`. Use the **Planner Prompt** from `references/prompts.md` to generate a `chapter_intent.md`.
- **Goal**: Define the scene goals, hooks to resolve, and new hooks to plant.

### Step 2: Composition (The Writer)
Read the `chapter_intent.md` and the relevant context from `world_state.json` and `character_matrix.json`. Use the **Writer Prompt** to generate the prose.
- **Target**: ~3000 words (or as requested). Focus on "Show, Don't Tell" and distinct character voices.

### Step 3: State Settlement (The Observer & Reflector)
Read the generated chapter. Use the **Observer Prompt** to extract all new facts, character changes, and hook updates.
- **Update**: Use `scripts/state_manager.py` to update the JSON files in `story/state/` with these changes. This ensures the next chapter has an accurate "truth state."

### Step 4: Auditing & Revision (The Auditor)
Use the **Auditor Prompt** to check the chapter against 33-dimensions of quality (pacing, logic, dialogue, etc.). 
- Detailed criteria: See `references/prompts.md` for the full checklist.
- If critical issues are found, perform a self-revision using the **Reviser Prompt**.
- Mark the chapter as "Settled" once it passes audit.

## 3) Truth Files Reference
- `world_state.json`: Locations, rules, systems (magic/tech), history.
- `character_matrix.json`: Attributes, motivations, relationships, current status.
- `subplot_board.json`: Hook ID, status (Active/Resolved/Stale), debt (how long it's been open).
- `chapter_summaries.json`: One-paragraph summary of each chapter's events.

## 4) Controlling the Narrative
- **Long-term**: Edit `author_intent.md` to change the book's destination.
- **Short-term**: Edit `current_focus.md` to steer the next 1-3 chapters (e.g., "focus on the training arc," "resolve the mentor conflict").

## Output Standards
- **Coherence**: Never contradict the `world_state.json` or `character_matrix.json`.
- **Pacing**: Avoid "pacing fatigue" (too much action or too much exposition in a row).
- **Hooks**: Always resolve hooks eventually; track "hook debt" in the audit.
