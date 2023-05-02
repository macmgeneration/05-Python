from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        params = parse_qs(query)
        text = params['text'][0] if 'text' in params else 'No se recibió ningún texto.'
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = f"El texto recibido es: {text}"
        self.wfile.write(bytes(message, "utf8"))

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, GetHandler)
    httpd.serve_forever()