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
