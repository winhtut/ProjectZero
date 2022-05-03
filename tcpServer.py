import socket
import bst_bst_db3
from bst_bst_db3 import searchingInDB

class TCPserver():
    def __init__(self):
        self.server_ip='localhost'
        self.server_port = 9998
    def main(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen(1)
        print(f'[*] Listening on {self.server_ip}:{self.server_port} >:')
        while True:
            client, address = server.accept()
            print(f'[*] Accepted connection from {address[0]}:{address[1]}')
            self.handle_client(client)

    def handle_client(self,client_socket):
        with client_socket as sock:
            request = sock.recv(4096)
            print(f'[*] Received: {request.decode("utf-8")}')
            clientInfo =request.decode("utf-8")
            print(type(clientInfo))
            c_username , c_password =clientInfo.split(" ")
            db_return =self.toDatabase(c_username)
            print(f'We Found !{db_return}')

            if db_return:
                db_return="We Found:"+db_return
                db_return:bytes = bytes(db_return, 'utf-8')
            # sock.send(b'ACK')

                sock.send(db_return)
            else:
                sock.send(b'Not Found!')
    def toDatabase(self,db_data):
        root =bst_bst_db3.dataInsertion()
        db_data=db_data.lower()
        firstData = db_data[0]
        flag  = searchingInDB(root,firstData,db_data)
        print("[*]We found",flag)
        return flag



if __name__ == '__main__':
    Myserver = TCPserver()
    Myserver.main()