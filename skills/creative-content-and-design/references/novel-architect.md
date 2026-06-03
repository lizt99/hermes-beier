# Novel Architect (Native Implementation)

## 1) Triage & Initialization
- Genre, Language, Core Concept.
- Workspace: `books/<book-id>/story/state/`.

## 2) The Writing Pipeline
1. **Planning**: Generate `chapter_intent.md`.
2. **Composition**: Generate prose (~3000 words).
3. **State Settlement**: Update JSON files via `scripts/state_manager.py`.
4. **Auditing**: 33-dimensions of quality check.

## 3) Truth Files
- `world_state.json`, `character_matrix.json`, `subplot_board.json`, `chapter_summaries.json`.
