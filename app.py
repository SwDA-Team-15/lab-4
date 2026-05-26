import http.server
import json
import os
import socket

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_COLOR = os.getenv("APP_COLOR", "blue")

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = json.dumps({"status": "ok"}).encode()
        elif self.path == "/":
            body = json.dumps({
                "version": APP_VERSION,
                "color": APP_COLOR,
                "hostname": socket.gethostname()
            }).encode()
        else:
            self.send_response(404)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    server = http.server.HTTPServer(("", 8080), Handler)
    print(f"Starting server v{APP_VERSION} ({APP_COLOR}) on port 8080")
    server.serve_forever()