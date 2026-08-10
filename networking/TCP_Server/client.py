import socket
import threading
def receive(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(f'received: {data.decode()}')
        except:
            break
    conn.close()
    print('Client Disconnected by server')

def send(conn):
    while True:
        try:
            message = input('enter message: ')
            if message.lower() == 'exit':
                conn.close()
                break
            conn.send(message.encode())
        except:
            break
def set_up():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8080))
    print(f'connected')
    return client
   
def main():
    client_server = set_up()
    receive_thread = threading.Thread(target=receive, args= ((client_server),))
    receive_thread.start()
    send(client_server)
    receive_thread.join()
main()