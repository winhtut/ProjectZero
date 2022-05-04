import socket
import bst_bst_db3
from bst_bst_db3 import searchingInDB , status , searchingInRLTTree,forLoginObj,RLTchecking

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
            c_username , c_password , option =clientInfo.split(" ")
            if option == "register":
                db_return =self.toDatabase(c_username,c_password)

                if db_return:
                    db_return="Registration Success Mr/Ms: "+db_return

                    db_return:bytes = bytes(db_return, 'utf-8')
            # sock.send(b'ACK')

                    sock.send(db_return)
            else:
                db_return = self.toDatabaseLogin(c_username, c_password)
                print("db return type",type(db_return))
                if db_return:
                    db_return = "Login Success  Mr/Ms: " + db_return
                    db_return: bytes = bytes(db_return, 'utf-8')
                    # sock.send(b'ACK')

                    sock.send(db_return)
                else:
                    db_return = "Login Failed!"
                    db_return: bytes = bytes(db_return, 'utf-8')
                    # sock.send(b'ACK')

                    sock.send(db_return)




    def toDatabase(self,db_data,db_pw):
        root =bst_bst_db3.dataInsertion()
        db_data=db_data.lower()
        firstData = db_data[0]
        searchingInDB(root,firstData,db_data,db_pw)
        if status.status == True:

            print("[*]Registration Success : ",db_data)
            return db_data
    def toDatabaseLogin(self,db_data,db_pw):

        db_data=db_data.lower()
        firstData = db_data[0]

        print("Lgoin Process")
        RLTchecking(forLoginObj.getTree())
        found_name =searchingInRLTTree(forLoginObj.getTree(),firstData,db_data,db_pw)
        print('found name',found_name)
        return found_name





if __name__ == '__main__':
    Myserver = TCPserver()
    Myserver.main()