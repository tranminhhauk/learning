import socket
def handle_request(conn):
    request = conn.recv(1024).decode()
    if not request:
        return
    line_request = request.split('\n')[0]
    print(line_request)
    parts = line_request.split(' ')
    if len(parts) >= 2:
        method = parts[0]
        path =  parts[1]
        if path == '/hello':
            body = 'Hello World'
            response = (
                'HTTP/1.1 200 OK\r\n'
                'Content-Type: text/plain\r\n'
                f'Content-Length: {len(body)}\r\n'
                '\r\n'
                f'{body}'
            )
            conn.send(response.encode())
        else:
            body = '404 Not Found'
            response = (
                 'HTTP/1.1 404 Not Found\r\n'
                 'Content-Type: text/plain\r\n'
                 f'Content-Length: {len(body)}\r\n'
                 '\r\n'
                 f'{body}'
            )
            conn.send(response.encode())
    conn.close()
def set_up():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8080))
    server.listen(5)
    print('server running\nwaiting connection')
    while True:
        conn, addr = server.accept()
        handle_request(conn)
set_up()