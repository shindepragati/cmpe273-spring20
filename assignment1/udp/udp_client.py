import socket
import time

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "ping";
send_againFlag = 0
prev_line=''
prev_id=0
count = 0

def send(filename):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        print("Connected to the server.")
        fileinput = open(filename, 'r')
        #with open("udp/upload.txt", 'r') as fileinput:
        print("Starting a file (upload.txt) upload...")
        for line in fileinput:
            s.settimeout(1.0)
            global prev_line,prev_id
            #print("lineee",line)
            prev_line=line
            prev_id=prev_id+1
            try:
                s.sendto(f"{prev_id}:{prev_line}".encode(), (UDP_IP, UDP_PORT))
                data, ip = s.recvfrom(BUFFER_SIZE)
                printRespose(data)
            except socket.timeout:
                resend()
            
        print("File upload successfully completed.")    
        s.close()

    except socket.error:
        print("Error! {}".format(socket.error))
      
def resend():
    global count
    count += 1
    while count <= 5:
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(1.0)
            s.sendto(f"{prev_id}:{prev_line}".encode(), (UDP_IP, UDP_PORT))
            print("Lost packet",prev_id)
            data, ip = s.recvfrom(BUFFER_SIZE)  
            if(len(data)==0 ):
                count += 1
            else:
                print(data)
                #send()
                break
        except socket.timeout:
            resend()
       

def printRespose(data):
    global prev_id
    temp=prev_id
    temp=temp*2
    if(len(data) > 0 and str(temp)==data.decode()):
        print("Received ack(",data.decode(),") from the server.")

send("/Users/karthikkathirvel/Desktop/GitHub_273/assignment/assignment1/udp/upload.txt")


    