from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <style>
            table{
                border-top: 10;
                border-bottom: 10;
                border-left: 10;
                border-right: 10;
                border-color: black;
            }
            td{
                background-color: aqua;
                font-size: medium;
            }
            th{
                background-color: lightblue;
                font-size: 20;
            }
        </style>
    </head>
    <body bgcolor="lightgray">
        <h1 style="color:darkgreen;text-align: center">TCP/IP Protocols - 24005057</h1>
        <table align="center" border="10" cellpadding="15" cellspacing="0" width=700>
            <tr">
                <th style="color:blue">Layer</th>
                <th style="color:blue">Protocol</th>
            </tr>
            <tr>
                <td>Application Layer</td>
                <td>HTTP, HTTPS, FTP, SMTP, DNS</td>
            </tr>
            <tr>
                <td>Transport Layer</td>
                <td>TCP, UDP, SCTP</td>
            </tr>
            <tr>
                <td>Internet Layer</td>
                <td>IP (IPv4, IPv6), ICMP, ARP</td>
            </tr>
            <tr>
                <td>Network Access Layer</td>
                <td>Ethernet, Wi-Fi, MAC, PPP</td>
            </tr>
            </th>
        </table>
    </body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running...")
httpd.serve_forever()
