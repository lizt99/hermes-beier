# Dispatching Parallel Agents

Dispatch one agent per independent problem domain. Let them work concurrently.

**Use when:**
- 3+ test files failing with different root causes
- Multiple subsystems broken independently
- No shared state between investigations

**Pattern:**
1. **Identify Independent Domains**: Group failures by subsystem/file.
2. **Create Focused Agent Tasks**: Specific scope, clear goal, constraints, expected output.
3. **Dispatch in Parallel**: All run concurrently.
4. **Review and Integrate**: Read summaries, verify no conflicts, run full suite.

**Agent Prompt Structure:**
- Focused scope.
- Self-contained context.
- Specific output expectations.
- Constraints (e.g., "Do NOT change production code").
