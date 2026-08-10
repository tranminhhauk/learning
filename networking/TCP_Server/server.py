import socket
import threading
def receive(conn):
    while True:
        try:
            data = conn.recv(1024) 
            if not data:
                break
            print(f"received: {data.decode()}")
            return data.decode()
        except Exception as e:
            print(e)
    conn.close()
    print('Client Disconnected, waiting connection')
def handle(conn):
    result = 0
    data = receive(conn)
    parts = data.split(' ')
    print(parts)
    if len(parts) >= 3:
        a = int(parts[0])
        b = parts[1]
        c = int(parts[2])
        if b == '-':
            result = a - c
        if b == '+':
            result = a + c
    return str(result)
def send_(conn):
    while True:
        try:
            message = handle(conn)           
            if message.lower() == 'exit':
                conn.close()
                print("server disconected")
                break
            conn.send(message.encode())
        except Exception as e:
            print(e)
            break
def set_up():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(5)
    print("server running, waiting connection")
    return server_socket
def client(conn, addr):
    print(f'Server connected with {addr}')
    send_thread =threading.Thread(target=send_, args=(conn, ))
    send_thread.start()
    receive_thread = threading.Thread(target=receive, args= (conn, )) ## receive
    receive_thread.start()
    receive_thread.join()
    send_thread.join()
    
def main(): 
    my_socket = set_up()
    while True:
        conn, addr = my_socket.accept()
        client_thread = threading.Thread(target= client, args= (conn, addr))
        client_thread.start()
main()
    