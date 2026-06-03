# Using Git Worktrees

**Core principle: Systematic directory selection + safety verification = reliable isolation.**

## Directory Selection
1. Check `.worktrees/` or `worktrees/`.
2. Check `CLAUDE.md`.
3. Ask User: `.worktrees/` (local) vs `~/.config/superpowers/worktrees/` (global).

## Safety Verification
- For project-local: **MUST** verify directory is ignored (`git check-ignore`).
- If not ignored: Add to `.gitignore`, commit, then proceed.

## Creation Steps
1. Detect project name.
2. Create worktree: `git worktree add <path> -b <branch>`.
3. Run project setup (`npm install`, `cargo build`, etc.).
4. Verify clean baseline (run tests).
5. Report location and status.
