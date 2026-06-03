---
name: infrastructure-and-setup
description: "Use when setting up ad-hoc servers, environment tools, or project-specific agent configurations. Covers: (1) quick-file-server for authenticated file sharing and (2) install-mspbots-agent for fetching configurations from the private npm registry."
---

# Infrastructure and Setup

Utilities for environment configuration and ad-hoc infrastructure.

## 1. Quick File Server (Python)
**Trigger**: When you need to provide ad-hoc, authenticated web access to a local directory.
- **Workflow**: Check directory → Select port (8080/8888) → Generate Basic Auth credentials → Deploy `scripts/serve_auth.py` → Run in background → Verify with curl.
- **Security**: Always use Basic Auth. Reminder: This is for temporary use over HTTP.
- **UTF-8**: Ensure the server sends `charset=utf-8` if content is non-ASCII.

## 2. MSPBots Agent Setup
**Trigger**: When you need to download and install agent configuration from `npm.mspbots.ai`.
- **Workflow**: Run `scripts/fetch_agent_config.py <AGENT_ID>`.
- **Action**: Extracts files (`AGENTS.md`, `tools.json`, `skills/`) directly into the current working directory.
- **Dependencies**: Python 3 and npm.

## Sub-Workflows (References)
- `references/file-server.md`: Port selection strategy and firewall pitfalls.
- `references/agent-install.md`: npm registry details and dependency requirements.
