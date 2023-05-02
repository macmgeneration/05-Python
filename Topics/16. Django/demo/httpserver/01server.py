from http.server import BaseHTTPRequestHandler, HTTPServer

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = "Hola! Este es un servidor HTTP personalizado en Python."
        self.wfile.write(bytes(message, "utf8"))

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, GetHandler)
    httpd.serve_forever()