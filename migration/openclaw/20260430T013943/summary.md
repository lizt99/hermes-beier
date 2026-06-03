# OpenClaw -> Hermes Migration Report

- Timestamp: 20260430T013943
- Mode: execute
- Source: `/home/mspbots/.openclaw`
- Target: `/home/mspbots/.hermes`

## Summary

- migrated: 6
- archived: 4
- skipped: 31
- conflict: 2
- error: 0

## Warnings

- Conflicts were found. Re-run with --overwrite to replace conflicting targets after item-level backups.
- A config.yaml write hit a conflict or error mid-apply; later config items were skipped to avoid a partial write.

## What Was Not Fully Brought Over

- `/home/mspbots/.openclaw/workspace/AGENTS.md` -> `(n/a)`: No workspace target was provided
- `/home/mspbots/.openclaw/openclaw.json` -> `/home/mspbots/.hermes/.env`: No Hermes-compatible messaging settings found
- `/home/mspbots/.openclaw/openclaw.json` -> `/home/mspbots/.hermes/.env`: No Discord settings found
- `/home/mspbots/.openclaw/openclaw.json` -> `/home/mspbots/.hermes/.env`: No Slack settings found
- `/home/mspbots/.openclaw/openclaw.json` -> `/home/mspbots/.hermes/.env`: No WhatsApp settings found
- `/home/mspbots/.openclaw/openclaw.json` -> `/home/mspbots/.hermes/.env`: No Signal settings found
- `/home/mspbots/.openclaw/openclaw.json` -> `/home/mspbots/.hermes/.env`: No provider API keys found
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `/home/mspbots/.openclaw/workspace/memory` -> `/home/mspbots/.hermes/memories/MEMORY.md`: No .md files found in workspace/memory/
- `(n/a)` -> `/home/mspbots/.hermes/tts`: Source directory not found
- `/home/mspbots/.openclaw/openclaw.json` -> `(n/a)`: Selected Hermes-compatible values were extracted; raw OpenClaw config was not copied.
- `/home/mspbots/.openclaw/credentials` -> `(n/a)`: Contains secrets, binary state, or product-specific runtime data
- `/home/mspbots/.openclaw/devices` -> `(n/a)`: Contains secrets, binary state, or product-specific runtime data
- `/home/mspbots/.openclaw/identity` -> `(n/a)`: Contains secrets, binary state, or product-specific runtime data
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `(n/a)` -> `(n/a)`: blocked by earlier apply conflict
- `/home/mspbots/.openclaw/workspace/SOUL.md` -> `/home/mspbots/.hermes/SOUL.md`: Target exists and overwrite is disabled
- `/home/mspbots/.openclaw/openclaw.json` -> `/home/mspbots/.hermes/config.yaml`: Model already set and overwrite is disabled

## Next Steps

- Review the migration report at /home/mspbots/.hermes/migration/openclaw/20260430T013943/summary.md
- Start a new Hermes session (or /reset) to pick up the imported config.
- Re-run with --overwrite to apply items that were blocked by conflicts.
