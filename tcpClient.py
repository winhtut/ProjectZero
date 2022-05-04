import  socket

class Client:
    def __init__(self,loginInfo):
        self.target_host ='localhost'
        self.target_port = 9998
        self.client_info =loginInfo
        self.ClientMessage =bytes(self.client_info,'utf-8')

    def runClient(self):
        client=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        client.connect((self.target_host,self.target_port))

        client.send(self.ClientMessage)

        recvFromServer=client.recv(4096)
        print(f'Back received from server: {recvFromServer.decode("utf-8")}')
        
        client.close()

def option():
    try:
        option = int(input("1:For Register:\n2: For Login"))
        if option==1:
            c_username = input("Enter username for RG:")
            c_password = input("Enter password For RG: ")
            client_info= c_username+" "+c_password+" "+"register"
            clineObj=Client(client_info)
            clineObj.runClient()
        else:
            c_username = input("Login username:")
            c_password = input("Login password :")
            client_info = c_username + " " + c_password + " " + "login"
            clineObj = Client(client_info)
            clineObj.runClient()
                # ယခု နေရာတွင် Registration ကို စစ်ဆေးရန် ရေးရမည်
    except Exception as err:
        print(err)
        print("Try Again ! Invalid Option ")


if __name__=="__main__":
    while True:
        option()



