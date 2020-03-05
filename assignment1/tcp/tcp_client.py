import socket
import sys
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE1 = 1024
BUFFER_SIZE2 = 1024
MESSAGE = "ping"


def send():
    id=sys.argv[1]
    delay=sys.argv[2]
    msgcount=sys.argv[3]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    
    count = 1
    while True:
        if(count <= int(msgcount)):
            print("sending data:", MESSAGE)
            s.send(f"{id}:{MESSAGE}".encode())
            data = s.recv(BUFFER_SIZE1)
            print("received data:", data.decode())
            count += 1
            time.sleep(int(delay))
        else:
           print("done bye")
           s.close()
           break 
    


send()


#def main():
    # creating thread 
   # reloader=False
   # t1 = threading.Thread(target=tcp_client1)
    #t2 = threading.Thread(target=tcp_client2) 
  
    # Start new Threads
   # t1.start()
   # t2.start()
    # wait until thread 1 is completely executed 
   # t1.join() 
    # wait until thread 2 is completely executed 
   # t2.join() 

#if __name__ == "__main__": 
 #   main()
 