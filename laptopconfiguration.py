from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
        <title> My Laptop Configuration</title>
    
    </head>
    <body>
        <h2 align="center"> HANNAH VASANTHI A</h2>
        <h2 align="center">Ref no : 26019069</h2>
        <h1 align="center">Laptop Configuration</h1>
        <table border="2" cellspacing="0" cellpadding="65">
            
            <tr>
                <th>S.N0</th>
                <th>DEVICE NAME</th>
                <th>PROCESSOR</th>
                <th>RAM</th>
                <th>GRAPHICS CARD</th>
                <th>STORAGE</th>
            </tr>
            <tr>
                <td>1</td>
                <td>TL15-53M-G2</td>
                <td>Intel&reg; Core&trade; 5 210H (2.20 GHz)</td>
                <td>16.0 GB</td>
                <td>128 MB</td>
                <td>477 GB</td>
            </tr>

        </table>
    
    </body>

        
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()