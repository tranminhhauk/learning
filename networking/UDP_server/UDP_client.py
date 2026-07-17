import socket
def UDP_client():
    
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(1)
    addr = ('localhost', 8888)
    while True:
        message = input('enter messgae: ')
        if message.lower() == 'exit':
            break
        client.sendto(message.encode(), addr)
        try:
            data, add = client.recvfrom(1024)
            print(f'server: {data.decode()} by {add}')
        except socket.timeout:
            print('Not received by server')
    client.close()
UDP_client()