import SimpleHTTPServer
import SocketServer
from http.server import HTTPServer, BaseHTTPRequestHandler
import redis

PORT = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler = SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
