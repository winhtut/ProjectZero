from bst_bst_dbII import root_length_tree

class CheckingStatus:
    def __init__(self):
        self.status =None
        self.LoginStatus=None

status =CheckingStatus()


class DataTree:
    def __init__(self):
        self.name=None
        self.pw=None
        self.d_left=None
        self.d_right=None

# class LengthTree:
#     def __init__(self):
#         self.l_lenght=None
#         self.l_right=DataTree()
#         self.l_left=DataTree()

class Node:
    def __init__(self,data):
        self.CharAlphbet=data
        self.c_right=None
        self.c_left=None
        
        self.RootLengthTree= root_length_tree.storeLengthTree()

class forLogin:
    def __init__(self,treeClone):
        self.TreeClone = treeClone
    def insert(self,rlt):

        self.TreeClone = rlt

    def getTree(self):
        return self.TreeClone

forLoginObj = forLogin('data')
def insertToRootLengthTree(data,db_pw):
    dataLength = len(data)
    nodeObj = Node(data)

    try:
        RLT = searchLenghtInRLT(data,dataLength,nodeObj.RootLengthTree,db_pw)
        forLoginObj.insert(RLT)


        print('Inserted at RootLenghtTree Just Showing Object Memory Address: ',RLT)

        print("message",status.status)
        RLTchecking(RLT)


    except Exception as err:
        print(err)
#Login
def insertToRootLengthTreeLogin(data,db_pw):
    dataLength = len(data)
    nodeObj=Node(data)
    try:
        RLT = searchLenghtInRLTLogin(data,dataLength,nodeObj.RootLengthTree,db_pw)

        print("Message Login :",status.LoginStatus)
        RLTchecking(RLT)


    except Exception as err:
        print(err)

def searchLenghtInRLT(data , dataLength,_RLT,db_pw):#for register


    if _RLT is not None:
        if _RLT.data==dataLength:

            print("working here!",_RLT.info)
            infoLength =len(_RLT.info)
            if infoLength == 0:
                _RLT.info.append(data)
                _RLT.infoPw.append(db_pw)
                print("Registration Success :", data,db_pw)
                status.status=True

                return _RLT
            else:
                for i in _RLT.info:
                    if i == data:
                        print("Already Exit!")
                        status.status=False

                        return _RLT
                _RLT.info[infoLength].append(data)
                _RLT.infoPw[infoLength].append(db_pw)
                print("Registration Success:", data , db_pw)
                status.status=True
                return _RLT

        if _RLT.data < dataLength :
            _RLT.right = searchLenghtInRLT(data , dataLength , _RLT.right,db_pw)
        else:
            _RLT.left = searchLenghtInRLT(data , dataLength , _RLT.left,db_pw)
    return _RLT

def searchLenghtInRLTLogin(data , dataLength,_RLT,db_pw): #for login


    if _RLT is not None:
        if _RLT.data==dataLength:

            print("working here! Checking For Login data: ",_RLT.info)
            z=0
            for i in _RLT.info:
                if i == data and _RLT.infoPw[z]==db_pw:
                    print("Login Success!")
                    status.LoginStatus=True
                    return _RLT
                z=z+1
            # if len(_RLT.info) == 0:
            #     _RLT.info.append(data)
            #     _RLT.infoPw.append(db_pw)
            #     print("Data Inserted :", data)
            #     status.status=True
            #
            #     return _RLT
            # else:
            #     for i in _RLT.info:
            #         if i == data:
            #             print("Already Exit!")
            #             status.status=False
            #
            #
            #             return _RLT
            #     _RLT.info.append(data)
            #     print("Data Inserted :", data)
            #     status.status=True

        if _RLT.data < dataLength :
            _RLT.right = searchLenghtInRLT(data , dataLength , _RLT.right,db_pw)
        else:
            _RLT.left = searchLenghtInRLT(data , dataLength , _RLT.left,db_pw)
    return _RLT

#SearchingInDB Lgoin
# def searchingInDBLogin(root, Oo, name,db_pw):
#     if root is not None:
#         currentValue = ord(root.CharAlphbet)
#         incomeValue = ord(Oo)
#
#         print(currentValue, incomeValue)
#         if currentValue == incomeValue:
#             print("We Found Data at searching in DB :",name,type(name))
#             # return name
#             # work here
#
#             insertToRootLengthTree(name,db_pw)
#
#         elif currentValue < incomeValue:
#             name1 =searchingInDBLogin(root.c_right, Oo, name,db_pw)
#             return name1
#         elif currentValue > incomeValue:
#             name2 = searchingInDBLogin(root.c_left, Oo, name,db_pw)
#             return name2
def searchingInRLTTree(root, firstdata, name,db_pw):
    if root is not None:
        currentValue = root.data
        incomeValue = ord(firstdata)

        # print(currentValue, incomeValue)
        if currentValue == incomeValue:
            print("We Found Data at searching in Lenght :")
            # return name
            # work here

            length =len(root.info)
            for i in length:
                if root.info[i]==name and root.infoPw[i]==db_pw:
                    status.LoginStatus=True
                    return name



        elif currentValue < incomeValue:
            searchingInRLTTree(root.right,firstdata,name,db_pw)

        elif currentValue > incomeValue:
            searchingInRLTTree(root.left, firstdata,name,db_pw)

    return name
def RLTchecking(RLT):
    if RLT is not None:
        RLTchecking(RLT.left)
        if len(RLT.info) != 0:
            print("\n For :",RLT.data)
            print("data are:",RLT.info)

        RLTchecking(RLT.right)

# def insertToRootLengthTree(data):
#     dataLength = len(data)
#     nodeObj=Node(data)
#     try:
#         RLT = searchLenghtInRLT(data,dataLength,nodeObj.RootLengthTree)
#         print('Inserted at RootLenghtTree',RLT)
#         RLTchecking(RLT)
#
#     except Exception as err:
#         print(err)
#
# def searchLenghtInRLT(data , dataLength,_RLT):
#
#     if _RLT is not None:
#         if _RLT.data==dataLength:
#
#             _RLT.info.append(data)
#
#         #     data ထည့်ပြီးသွားလျင် ပြန်ပြီး root တစ်ခုလုံးကို update မလုပ်နိုင်သေး
#
#         if _RLT.data < dataLength :
#             _RLT.right = searchLenghtInRLT(data , dataLength , _RLT.right)
#         else:
#             _RLT.left = searchLenghtInRLT(data , dataLength , _RLT.left)
#     return _RLT

def dataInsertion():
    
    root=Node('p')
    
    root.c_left=Node('h')
    root.c_left.c_left=Node('d')
    root.c_left.c_right=Node('l')
    root.c_left.c_left.c_left=Node('b')
    root.c_left.c_left.c_right=Node('f')
    root.c_left.c_right.c_left=Node('j')
    root.c_left.c_right.c_right=Node('n')
    root.c_left.c_left.c_left.c_left=Node('a')
    root.c_left.c_left.c_left.c_right=Node('c')
    root.c_left.c_left.c_right.c_left=Node('e')
    root.c_left.c_left.c_right.c_right=Node('g')

    root.c_left.c_right.c_left.c_left=Node('i')
    root.c_left.c_right.c_left.c_right=Node('k')
    root.c_left.c_right.c_right.c_left=Node('m')
    root.c_left.c_right.c_right.c_right=Node('o')


    root.c_right=Node('t')
    root.c_right.c_left=Node('r')

    root.c_right.c_right=Node('x')

    root.c_right.c_left.c_left=Node('q')
    root.c_right.c_left.c_right=Node('s')

    root.c_right.c_right.c_left=Node('v')
    root.c_right.c_right.c_right=Node('y')

    root.c_right.c_right.c_left.c_left=Node('u')
    root.c_right.c_right.c_left.c_right=Node('w')

    root.c_right.c_right.c_right.c_right=Node('z')
    return root

def inorder(root):
    if root is not None:
        inorder(root.c_left)
        print((root.CharAlphbet)+'->',end=' ')
        inorder(root.c_right)

def searching(root,Oo,name):
    if root is not None:
        currentValue=ord(root.CharAlphbet)
        incomeValue=ord(Oo)
    
        
        print(currentValue,incomeValue)
        if currentValue==incomeValue:
            print("We Found Data")
            #work here

            insertToRootLengthTree(name)

        elif currentValue < incomeValue:
            searching(root.c_right,Oo,name)
        elif currentValue > incomeValue:
            searching(root.c_left,Oo,name)


def searchingInDB(root, Oo, name,db_pw):
    if root is not None:
        currentValue = ord(root.CharAlphbet)
        incomeValue = ord(Oo)

        print(currentValue, incomeValue)
        if currentValue == incomeValue:
            print("We Found Data at searching in DB :",name,type(name))
            # return name
            # work here

            insertToRootLengthTree(name,db_pw)

        elif currentValue < incomeValue:
            name1 =searchingInDB(root.c_right, Oo, name,db_pw)
            return name1
        elif currentValue > incomeValue:
            name2 = searchingInDB(root.c_left, Oo, name,db_pw)
            return name2



if __name__ == "__main__":
    root=dataInsertion()
    inorder(root)
    while True:
        name=input("Please enter name!")
        name = name.lower()

        Oo=name[0]

        flag = searching(root,Oo,name)

        


        
