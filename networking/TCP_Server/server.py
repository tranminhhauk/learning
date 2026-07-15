import socket
import threading
def receive(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(f"received: {data.decode()}")
        except: 
            break
    conn.close()
    print('Client Disconnected, waiting connection')
def send(conn):
    while True:
        try:
            message = input('enter message: ')
            if message.lower() == 'exit':
                conn.close()
                print("server disconected")
                break
            conn.send(message.encode())
        except:
            break
def set_up():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(5)
    print("server running, waiting connection")
    return server_socket
def client(conn, addr):
    print(f'Server connected with {addr}')
    server_thread = threading.Thread(target=receive, args= ((conn, )))
    server_thread.start()
    send_thread =threading.Thread(target=send, args=((conn, )))
    send_thread.start()
    send_thread.join()
    send_thread.join()
def main(): 
    my_socket = set_up()
    while True:
        conn, addr = my_socket.accept()
        client_thread = threading.Thread(target= client, args= ((conn, addr)))
        client_thread.start()        
main()
