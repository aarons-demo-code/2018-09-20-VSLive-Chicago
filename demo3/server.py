import SimpleHTTPServer
import SocketServer
from http.server import HTTPServer, BaseHTTPRequestHandler
import redis

PORT = 8000

r = redis.StrictRedis(host='localhost', port=6379, db=0)

counter = 1

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        r.Set("thecounter", counter)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hey VSLive! thecounter = ' + counter)

# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler = SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
