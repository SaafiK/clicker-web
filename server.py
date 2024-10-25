import http.server
import socketserver

counter = 0  # Global counter to keep track of clicks


class MyHandler(http.server.SimpleHTTPRequestHandler):

    # Handle POST requests
    def do_POST(self):
        global counter

        # Check if the POST request is to '/increment'
        if self.path == '/increment':
            counter += 1  # Increment the counter
            # Send a response back with the updated counter
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(counter).encode('utf-8'))
        else:
            self.send_error(404, "File not found")  # Return 404 if unknown route

    # Handle GET requests
    def do_GET(self):
        # Serve the HTML file when the browser makes a GET request to "/"
        if self.path == "/":
            self.path = "index.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


# Set up the server
PORT = 8000
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
