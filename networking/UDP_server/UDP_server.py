import socket
def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('localhost', 8888))
    print('UDP running')
    while True:
        data, addr = server.recvfrom(1024)
        print(f'received {addr}: {data.decode()}')

        server.sendto("Ok".encode(), addr)
udp_server()