import http.server
import base64
import os
import sys

# These would be replaced by the agent during deployment
USERNAME = '{{username}}'
PASSWORD = '{{password}}'
DIRECTORY = '{{directory}}'
PORT = {{port}}

class AuthHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="Project Access"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        auth_header = self.headers.get('Authorization')
        encoded_creds = base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()
        if auth_header is None or auth_header != f'Basic {encoded_creds}':
            self.do_AUTHHEAD()
            self.wfile.write(b'Authentication required.')
        else:
            # Fix charset for .md and .txt files to handle non-ASCII characters (e.g. Chinese)
            if self.path.endswith('.md') or self.path.endswith('.txt'):
                full_path = self.translate_path(self.path)
                if os.path.isfile(full_path):
                    self.send_response(200)
                    ctype = 'text/markdown' if self.path.endswith('.md') else 'text/plain'
                    self.send_header('Content-type', f'{ctype}; charset=utf-8')
                    
                    with open(full_path, 'rb') as f:
                        fs = os.fstat(f.fileno())
                        self.send_header("Content-Length", str(fs[6]))
                        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
                        self.end_headers()
                        self.wfile.write(f.read())
                        return
            super().do_GET()

    def do_HEAD(self):
        self.do_GET()

if __name__ == "__main__":
    if not os.path.exists(DIRECTORY):
        print(f"Error: {DIRECTORY} does not exist.")
        sys.exit(1)
    
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, AuthHandler)
    print(f"Serving {DIRECTORY} on port {PORT}...")
    httpd.serve_forever()
