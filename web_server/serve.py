import http.server
import base64
import os

USERNAME = 'belle'
PASSWORD = 'shangan-password-666'
DIRECTORY = '/home/mspbots/workspace/project-shang-an/'
PORT = 80

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
            # Fix charset for .md and .txt files
            if self.path.endswith('.md') or self.path.endswith('.txt'):
                self.send_response(200)
                self.send_header('Content-type', 'text/markdown; charset=utf-8' if self.path.endswith('.md') else 'text/plain; charset=utf-8')
                
                full_path = os.path.join(DIRECTORY, self.path.lstrip('/'))
                if os.path.isfile(full_path):
                    with open(full_path, 'rb') as f:
                        content = f.read()
                        self.send_header('Content-Length', str(len(content)))
                        self.end_headers()
                        self.wfile.write(content)
                        return
                else:
                    self.send_error(404, "File not found")
                    return
            super().do_GET()

    # Also handle HEAD and POST if needed, but for viewing GET is enough.
    def do_HEAD(self):
        self.do_GET()

if __name__ == "__main__":
    # Ensure directory exists
    if not os.path.exists(DIRECTORY):
        print(f"Error: {DIRECTORY} does not exist.")
        exit(1)
    
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, AuthHandler)
    print(f"Serving {DIRECTORY} on port {PORT}...")
    httpd.serve_forever()
