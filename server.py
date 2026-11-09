# importing all the functions 
# from http.server module
from http.server import *

# creating a class for handling 
# basic Get and Post Requests
class Server(BaseHTTPRequestHandler):
  
    # creating a function for Get Request
    def do_GET(self):
      
        # Success Response --> 200
        self.send_response(200)
        
        # Type of file that we are using for creating our
        # web server.
        self.send_header('content-type', 'text/html')
        self.end_headers()
        
        # what we write in this function it gets visible on our
        # web-server
        self.wfile.write('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0">
  <title>Сходки</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;

      color: #ddd;
      background-color: #222;
    }
  </style>
  <script defer src="script.js"></script>
</head>
<body>
  <main>Сходки placeholder backend</main>
</body>
</html>
'''.encode())


# this is the object which take port 
# number and the server-name
# for running the server
port = HTTPServer(('', 5555), Server)

# this is used for running our 
# server as long as we wish
# i.e. forever
port.serve_forever()