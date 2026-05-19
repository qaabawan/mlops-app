from http.server import BaseHTTPRequestHandler, HTTPServer

class MLOpsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # A simple response message simulating a model deployment pipeline
        message = """
        <html>
            <head><title>MLOps Pipeline Status</title></head>
            <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
                <h1 style="color: #2E7D32;">🚀 MLOps Pipeline Successful!</h1>
                <p>Your application is successfully containerized via Docker and running inside WSL Ubuntu.</p>
                <p><b>Next Step:</b> Connect this to the automated Jenkins pipeline.</p>
            </body>
        </html>
        """
        self.wfile.write(bytes(message, "utf8"))

def run():
    print("Starting server on port 80...")
    server_address = ('', 80)
    httpd = HTTPServer(server_address, MLOpsHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
