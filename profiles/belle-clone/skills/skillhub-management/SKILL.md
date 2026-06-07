---
name: skillhub-management
description: Workflow for installing external skills via SkillHub CLI, migrating them to the Hermes profile, and fixing npm global permissions (e.g., mcporter EACCES).
---
# SkillHub Management

This skill outlines the workflow for installing skills via SkillHub and resolving common environment/permission issues encountered during setup (e.g., NPM global install errors).

## Trigger
When the user asks to install a skill via SkillHub (skillhub.cn) or mentions installing `tencent-docs` or other third-party MCP skills.

## Installation Workflow
1. **Check/Install CLI**: 
   Run `~/.local/bin/skillhub --version` or `command -v skillhub`.
   If missing, install via the official script (CLI only): 
   `curl -fsSL https://skillhub-1388575217.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash -s -- --cli-only`
2. **Install Skill**: 
   `~/.local/bin/skillhub install <skill-name>`
3. **Migrate to Profile (Critical)**: 
   SkillHub defaults to downloading skills into `/home/mspbots/skills/`. For Hermes Agent to recognize them, they MUST be moved into the current profile's skill directory:
   `mv /home/mspbots/skills/<skill-name> ~/.hermes/profiles/belle-clone/skills/`
4. **Verify**:
   Use `skill_view(name='<skill-name>')` to confirm it loaded successfully.

## Pitfalls & Workarounds

### NPM Global Install Permissions (EACCES)
Many SkillHub skills (like `tencent-docs`) rely on Node.js wrappers like `mcporter`. 
If you attempt to run `npm install -g <package>` and it fails with `EACCES: permission denied` on `/usr/lib/node_modules`, **DO NOT** attempt to use `sudo`. Instead, configure a local NPM prefix:
```bash
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
npm install -g mcporter
```
*Note: Always remember to prefix subsequent commands with `export PATH=~/.npm-global/bin:$PATH` if they rely on the newly installed global binaries in the same terminal session.*

### MCPorter Configuration
If configuring an MCP server that uses `mcporter` (like `tencent-docs`), ensure you use the correct local binary path to add the config:
```bash
export PATH=~/.npm-global/bin:$PATH
mcporter config add <server-name> "<api-url>" --header "Authorization=<token>" --transport http --scope home
```