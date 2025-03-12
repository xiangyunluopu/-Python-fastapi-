import socket

sock = socket.socket()

sock.bind(('localhost', 8084))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print('客户端发送的请求信息: ', data)
    conn.send(b'HTTP/1.1 200 ok\r\nserver:xiangyunluopu\r\nContent-Type:text/plain\r\n\r\nhello,world!')
    conn.close