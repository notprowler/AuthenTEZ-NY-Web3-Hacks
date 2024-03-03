import http.server
import socketserver
import urllib.parse

PORT = 8000

# Function to check if the SHA256 hash exists in the database file
def check_sha256_exists(sha256_hash, database_file="sha256_database.txt"):
    with open(database_file, "r") as file:
        for line in file:
            if sha256_hash in line.strip():
                return True
    return False

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/verify/"):
            # Extract the 256 characters after "/verify/"
            sha256 = self.path[len("/verify/"):len("/verify/") + 256]

            exists = check_sha256_exists(sha256)

            if len(sha256) == 256 and check_sha256_exists(sha256):
                self.path = '/real_product.html'
            elif len(sha256) != 256:
                self.path = '/wrong_code.html'
            else:
                self.path = '/fake_product.html'
            
            return super().do_GET()
        
        elif self.path == "/verify" or self.path == "/verify/":
            self.path = '/index.html'
            super().do_GET()
        else:
            # Call the superclass method for any other resource
            super().do_GET()

# Use the custom handler
httpd = socketserver.TCPServer(("", PORT), MyRequestHandler)

print(f"Serving at port {PORT}")
httpd.serve_forever()
