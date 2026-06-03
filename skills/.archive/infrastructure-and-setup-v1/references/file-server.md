# Quick File Server

## Workflow
1. **Directory Check**.
2. **Port Selection**: 8080, 8888, 3000. Avoid 40000+.
3. **Credentials**: Always use Basic Auth.
4. **Deployment**: `scripts/serve_auth.py`.
5. **Execution**: `terminal(background=True)`.
6. **Verification**: `curl -I localhost:<port>`.

## Pitfalls
- **Firewalls**: Cloud providers block ports by default.
- **UTF-8**: Default Python server might need charset override for non-ASCII.
