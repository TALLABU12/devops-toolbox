from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

class APIHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"status": "ok", "message": "API DevOps fonctionnelle", "version": "1.0"}
        self.wfile.write(json.dumps(response).encode())

HTTPServer(('0.0.0.0', 5000), APIHandler).serve_forever()
