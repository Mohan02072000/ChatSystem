import socket
import threading

csoc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Give data to connec to server: \n")
ipadd=input("Give IP address or name: ")
port=int(input("Give port number: "))
csoc.connect((ipadd,port))
print('connection successful')


    

def recv_msg():
    while True:
        reply=csoc.recv(1080).decode('utf-8')
        print(f'[REPLY FROM SERVER] {reply}')

    
recv_thread=threading.Thread(target=recv_msg)
recv_thread.start()
while True:
    msg=input()
    csoc.send(bytes(msg,'utf-8'))
    if(msg=="!disconnect"):
        csoc.close()
        break
print('[DISCONNECTION REQUST RECIEVED]')



