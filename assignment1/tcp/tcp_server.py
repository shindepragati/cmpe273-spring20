import socket
import threading 


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
clients={}


client_lock = threading.Lock() 

def listen_forever(conn,addr):
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: 
           print('No data received.')
           client_lock.release() 
           break
        print(f"received data:{data.decode()}")
        conn.send("pong".encode())

    conn.close()


def Main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(2)
    print(f'Server started at port:{TCP_PORT}')
    while True: 
        conn, addr = s.accept() 
        client_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        threading._start_new_thread(listen_forever, (conn,addr)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 