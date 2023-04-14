import socket
import threading

SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket creation succesfull \n")
print("Socket is active \n")
ipadd=input("Input Server IP Adress: ")
port=int(input("Input Port Number (4 digits): "))
SERVER.bind((ipadd,port))


def handle_client(conn,addr):
    print(f"[NEW CONNECTION FOUND] {addr} connected")
    def send_msg():
        while True:
            sd=input(f'[REPLYING TO] {addr}')
            conn.send(bytes(f'[SERVER REPLY] : {sd}','utf-8'))
            print(f'[MESSAGE SENT TO CLIENT] {addr} {sd}')
    send_thread=threading.Thread(target=send_msg)
    send_thread.start()
    while True:
        msg=conn.recv(1080).decode('utf-8')
        print(f"[MESSAGE RECIEVED]{addr} :{msg}") 
        if(msg=="!disconnect"):
            break
    conn.close()
    print(f"[CLIENT DISCONNECTED] {addr}")
    
   

def launch_server():
    SERVER.listen()
    print(f"[SERVER LISTNING] at IP {ipadd} and port {port}")
    
    while True:
        conn , addr= SERVER.accept()
        thread=threading.Thread(target=handle_client, args=((conn,addr)))
        thread.start()
        
        

print("[LAUNCHING SERVER]")
launch_server()
