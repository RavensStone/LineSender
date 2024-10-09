# receiver.py

from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # Get the size of data
        post_data = self.rfile.read(content_length).decode('utf-8')  # Read and decode the received data
        print(f"Received string: {post_data}")

        # Send response back to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Data received successfully")


def run(server_class=HTTPServer, handler_class=RequestHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        print(f"Server running on port {port}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
        httpd.server_close()


if __name__ == '__main__':
    run()
