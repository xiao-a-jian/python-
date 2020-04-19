"""
http
"""
from socket import *

s = socket()
s.bind(("0.0.0.0", 8000))
s.listen(3)

c, addr = s.accept()


data = c.recv(2048)
print(data.decode())

http_data = """HTTP/1.1 200 OK
Content-Type:text/html

hello world
"""

c.send(http_data.encode())

s.close()
c.close()



