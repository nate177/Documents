from http.server import HTTPServer, BaseHTTPRequestHandler


class echoHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type', 'text/html')
		self.end_headers()
		self.wfile.write(self.path.encode())


def main():
	PORT = 8000
	server =HTTPServer(('', PORT), echoHandler)
	print('server running on port %s' % PORT)
	server.serve_forever()


if __name__ == '__main__':
    main()
