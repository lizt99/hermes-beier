---
name: quick-file-server
description: Create a lightweight Python web server with Basic Auth for ad-hoc file browsing.
---

# quick-file-server

Provide ad-hoc, authenticated web access to a local directory for remote viewing and downloading.

## Trigger
- User asks to "create a web server" to "view files" or "access a directory" via browser.
- Need for a lightweight, zero-dependency file sharing solution on a remote machine.

## Workflow

1.  **Directory Check**: Verify the target directory exists and is readable.
2.  **Port Selection**:
    - Use `ss -tuln` to check for available ports.
    - Prefer standard "dev" ports like `8080`, `8888`, or `3000`.
    - Avoid very high random ports (e.g., 40000+) as they are frequently blocked by cloud provider firewalls.
    - If 8080 is blocked, try port `80` (requires `sudo`).
3.  **Credential Generation**:
    - Ask the user for a username/password or generate strong temporary ones.
    - **Always** use at least Basic Auth to prevent unauthorized indexing/access.
4. **Deployment**:
    - **MUST USE TEMPLATE**: DO NOT write the script from scratch. Read `templates/serve_auth.py` via `skill_view(name='quick-file-server', file_path='templates/serve_auth.py')`, replace the `{{username}}`, `{{password}}`, `{{directory}}`, and `{{port}}` placeholders, and write it to disk. This template already includes critical fixes for UTF-8 encoding (Mojibake prevention).
5.  **Execution**:
    - Run the script in the background using `terminal(background=True)`.
    - Use `notify_on_complete: false` if it's meant to stay up.
6.  **Verification**:
    - Use `curl -I http://localhost:<port>` to verify the 401 Unauthorized response.
    - Get the public IP via `curl ifconfig.me`.
7.  **Handover**: Provide the user with the URL (`http://<public-ip>:<port>`), username, and password.

## Pitfalls
- **Firewalls**: Cloud instances (GCP, AWS) usually block all ports by default except 22, 80, 443. 8080 is often pre-opened or easier to open. If the user can't connect, suggest checking "Inbound Firewall Rules".
- **Process Death**: Ensure the process runs in the background. If the session context is fragile, use `nohup` or a screen/tmux session if available, though `background=True` in Hermes usually suffices for the session duration.
- **Security**: Basic Auth sends credentials in plain text over HTTP. Remind the user this is for convenience and "temporary/private" use, not for sensitive production data.
- **Character Encoding**: Python's `http.server` defaults to `Latin-1` for many text types. If the directory contains Chinese or other non-ASCII content (especially in `.md` or `.txt` files), ensure the server sends `charset=utf-8` in the `Content-type` header.

## Linked Files
- `templates/serve_auth.py`: Python script template for an authenticated file server.
