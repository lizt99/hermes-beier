---
name: agentic-software-development
description: "Use when starting any software development task, from design to implementation and verification. This umbrella skill covers the full Agentic Lifecycle: Brainstorming (Design), Planning, Execution (including Parallel Agents), Code Review, Verification, and Branch Completion."
---

# Agentic Software Development (Superpowers)

This skill provides a comprehensive methodology for agents to work on software projects with high discipline, isolation, and verification.

## Core Mindset

1. **Invoke Skills Proactively**: If there is even a 1% chance a skill applies, you MUST invoke it. Use the `Skill` tool before ANY response, including clarifying questions.
2. **Evidence Over Assertions**: Never claim work is complete without fresh verification evidence.
3. **Isolation**: Use git worktrees to isolate feature work.
4. **Decomposition**: Break complex tasks into bite-sized, independent plans.
5. **Priority**: User instructions > Superpowers skills > Default system prompt.

## The Agentic Lifecycle

### 1. Design & Brainstorming
**Trigger**: Before any creative work, building components, or modifying behavior.
- **Action**: Explore intent, requirements, and design before implementation.
- **Hard Gate**: Do NOT write code until a design doc is approved and committed to `docs/superpowers/specs/`.
- **Workflow**: Context check → Clarifying questions (one by one) → Approach proposals → Design presentation → Approval → Spec self-review → Write Plan.

### 2. Planning & Execution
**Trigger**: When starting implementation of an approved design.
- **Action**: Use `writing-plans` (external skill) to create a detailed task list.
- **Isolated Workspace**: Use **Git Worktrees** (`using-git-worktrees`) to ensure clean state and easy cleanup.
- **Execution**: Follow the plan exactly. Mark tasks `in_progress` and `completed` immediately.
- **Parallelization**: When facing 2+ independent tasks, use **Parallel Agents** (`dispatching-parallel-agents`) to work concurrently.

### 3. Review & Verification
**Trigger**: When receiving feedback or finishing a task.
- **Code Review**: When receiving review feedback (`receiving-code-review`), avoid performative agreement. Verify suggestions against the codebase. Push back with technical reasoning if a suggestion is YAGNI or incorrect.
- **Verification**: Before claiming ANY status or completion (`verification-before-completion`), run the FULL command and read the output. "Fresh evidence before claims."

### 4. Completion & Integration
**Trigger**: When all tasks are done and verified.
- **Finish Branch**: Use `finishing-a-development-branch`.
- **Steps**: Verify tests on result → Determine base branch → Present 4 options (Merge locally, PR, Keep, Discard) → Execute choice → Cleanup worktree.

## Meta: Writing Skills
**Trigger**: When a complex task succeeds or a new workflow is discovered.
- **Action**: Use `writing-skills` to capture the process. Follow the "Iron Law": No skill without a failing test (RED) baseline first.

## Specialized Engineering (DevOps, Debugging, TDD)
- **TDD**: Use `test-driven-development` for all new features and bugfixes.
- **Debugging**: Use `systematic-debugging` for root-cause analysis and `python-debugpy` / `node-inspect-debugger` for deep dives.
- **Project Structure**: Use `codebase-inspection` to understand unfamiliar projects.
- **Experimental Work**: Use `spike` for throwaway prototypes before committing to a design.

## Sub-Workflows (References)

Detailed instructions for each phase are available in the following references:
- `references/brainstorming.md`: Design-first workflow and "Visual Companion" rules.
- `references/parallel-agents.md`: Strategy for dispatching and integrating subagents.
- `references/plan-execution.md`: Reviewing and following implementation plans.
- `references/code-review.md`: Discipline for receiving and applying feedback.
- `references/verification.md`: Iron Law of verification and rationalization counters.
- `references/worktrees.md`: Directory selection and safety verification for git worktrees.
- `references/finishing-branches.md`: Branch completion options and cleanup protocol.
- `references/writing-skills.md`: TDD for documentation and Claude Search Optimization (CSO).
- `references/superpowers.md`: Skill discipline, red flags, and rationalization counters.
