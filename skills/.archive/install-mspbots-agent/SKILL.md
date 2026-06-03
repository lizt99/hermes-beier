---
name: install-mspbots-agent
description: Fetch agent configuration and files from the MSPBots npm registry.
---

# Install MSPBots Agent

## Overview

This skill allows you to download and install agent configuration and associated files from the MSPBots private npm registry (`https://npm.mspbots.ai/`) using an Agent ID.

## Usage

### Install Agent

Run the `fetch_agent_config.py` script with the target Agent ID. The script will look for a package named `@agent/<agent-id>`.

The script extracts the files directly into the **current working directory**, replacing or merging with any existing files.

```bash
# Basic usage
python skills/install-mspbots-agent/scripts/fetch_agent_config.py <AGENT_ID>
```

### Output Structure

The script extracts the contents of the downloaded npm package directly into the directory where the script is executed.

Example structure (if run in `/home/mspbots/.openclaw/workspace`):
```
/home/mspbots/.openclaw/workspace/
- AGENTS.md
- tools.json
- skills/
   - SKILL.md
```

## Dependencies

This script requires:
- `python3`
- `npm` (Node.js) installed and available in your PATH.

The python script itself uses only standard library modules (`argparse`, `os`, `shutil`, `subprocess`, `tarfile`, `tempfile`, `pathlib`).
