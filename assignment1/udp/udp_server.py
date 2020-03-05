import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
#MESSAGE = "pongg"

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    print("Server started at port",UDP_PORT)
    print("Accepting a file upload...") 
    try:
        while True:
            # get the data sent to us
            data, ip = s.recvfrom(BUFFER_SIZE)
          
            rec_str = data.decode(encoding="utf-8").strip()  
            str1=rec_str.split(':',1)
            temp=int(str1[0])*2                 
            temp=str(temp)
            #print("------"+str1[1])
            if(str1[1].startswith("9987")):   #example of lost packet
                temp=""
            else:
                s.sendto(temp.encode(), ip)
            if(temp=="20000"):
                print("Upload successfully completed.")
    except Exception:
        print("Error!",Exception)
        exit()

listen_forever()