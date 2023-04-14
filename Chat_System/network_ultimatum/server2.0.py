import socket
import os
import threading


SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket creation succesfull \n")
print("Socket is active \n")
ipadd=input("Input Server IP Adress: ")
port=int(input("Input Port Number (4 digits): "))
SERVER.bind((ipadd,port))
client_arr=[]


class client:
    conn=()    
    def name():
        return conn
    def connect(addr,rport):
        pass
    def init(self):
        client=SERVER.


def launch_server():
    SERVER.listen()
    print(f"[SERVER LISTNING] at IP {ipadd} and port {port}")
    
    while True:
        conn , addr= SERVER.accept()
        obj=client()
        obj.conn=conn
        
   

    
