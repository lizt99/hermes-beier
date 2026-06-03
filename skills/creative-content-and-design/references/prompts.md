# Novel Architect Prompts

## 1. Planner (Chapter Intent)
Generate the `chapter_intent.md` for the next chapter.
Context:
- `author_intent.md`: Long-term vision.
- `current_focus.md`: Immediate goals.
- `subplot_board.json`: Active/pending hooks.
- `chapter_summaries.json`: Last 3 chapters.

Output:
- Chapter Goal: What must change?
- Scene Breakdown: 3-5 beats.
- Hooks to Resolve: (From Subplot Board).
- New Hooks to Plant: (Cliffhangers/Promises).

## 2. Writer (Prose Generation)
Write the full chapter based on the `chapter_intent.md`.
Context:
- `world_state.json`: Local settings/rules.
- `character_matrix.json`: Current state/relations.
- Previous chapter's ending.

Style:
- High variance, low repetition.
- Show-don't-tell focused.
- Strong scene openers.

## 3. Observer (Fact Extraction)
Read the chapter and extract all *new* facts, character changes, and hook status.
Output as JSON:
{
  "characters": { "Name": { "status": "...", "location": "..." } },
  "subplots": { "HookID": "resolved|mentioned|deferred" },
  "world": { "NewLocation": "..." }
}

## 4. Auditor (33-Dimension Check)
Check the chapter against these 33 points (abbreviated):
- **Hook Debt**: Did you plant too many without resolving?
- **Character OOC**: Is their behavior consistent with the matrix?
- **Pacing Fatigue**: Are there 3+ consecutive chapters of high/low intensity?
- **Repetition**: Count "she said", "he felt", "however".
- **World Consistency**: Did the magic system break?

## 5. Normalizer (Length Control)
Adjust the chapter length to match the target word count (e.g., 3000 words).
- If too short: Expand scenes with sensory details, subtext, or dialogue.
- If too long: Condense redundant descriptions, merge short scenes, or trim dialogue.
Important: Do NOT lose plot points.

