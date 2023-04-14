import socket
import threading


class client(conn):
    name=''
    ip=''
    port=''
    def client(n,addr):
        name=n
        ip=addr[0]
        port=addr[1]
    def name(self):
        return name
    
    def send(self):
        pass
    
    def recv(self):
        pass
    def get_stats(self):
        return {'name':name,'ip':ip,'port':port}
    def connect(self):
        pass

class server:
    name=''
    ip=''
    port=''
    def server(n,i,p):
        name=n
        ip=i
        port=int(p)
    def get_stat(self):
        return {'name':name,'ip':ip,'port':port}
    def init(self):
        serv_obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("Socket creation succesfull")
        serv_obj.bind((ip,port))
        print('socket binding successful')
        print(f'[SERVERS STATUS] {get_stat}')
    def run(self):
        serv_obj.listen()
        while True:
            addr,conn=serv_obj.accept()
            thread=threading.Thread(target=handle_client, args=((conn,addr)))
            thread.start()
    def handle_client(conn,addr):
        print(f"[NEW CONNECTION FOUND] {addr} connected")

        conn.close()
        print(f"[CLIENT DISCONNECTED] {addr}")
 
