---
name: platform-and-infrastructure-setup
description: "Umbrella skill for environment configuration, ad-hoc infrastructure, and workspace setup. Covers: (1) quick-file-server for authenticated file sharing, (2) install-mspbots-agent for fetching configurations, and (3) general platform setup (GitHub, MCP, Webhooks)."
---

# Platform and Infrastructure Setup

Utilities and workflows for environment configuration and ad-hoc infrastructure.

## 1. Quick File Server (Python)
**Trigger**: When you need to provide ad-hoc, authenticated web access to a local directory.
- **Workflow**: Check directory → Select port (8080/8888) → Generate Basic Auth credentials → Deploy `scripts/serve_auth.py` → Run in background → Verify with curl.
- **Security**: Always use Basic Auth. Reminder: This is for temporary use over HTTP.

## 2. MSPBots Agent Setup
**Trigger**: When you need to download and install agent configuration from `npm.mspbots.ai`.
- **Workflow**: Run `scripts/fetch_agent_config.py <AGENT_ID>`.
- **Action**: Extracts files (`AGENTS.md`, `tools.json`, `skills/`) directly into the current working directory.

## 3. Platform & Workspace Tools
- **GitHub Auth**: Use `github-auth` to set up SSH keys or tokens.
- **MCP Servers**: Use `native-mcp` to connect to external tool providers.
- **Webhooks**: Use `webhook-subscriptions` for event-driven agent triggers.
- **Hermes Config**: Use `hermes-agent` for managing agent settings and tools.

## Sub-Workflows (References)
- `references/file-server.md`: Port selection strategy and firewall pitfalls.
- `references/agent-install.md`: npm registry details and dependency requirements.
- `references/github-setup.md`: Best practices for repository and auth management.
