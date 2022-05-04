from bst_bst_dbII import root_length_tree


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

def insertToRootLengthTree(data):
    dataLength = len(data)
    nodeObj=Node(data)
    try:
        RLT = searchLenghtInRLT(data,dataLength,nodeObj.RootLengthTree)
        print('Inserted at RootLenghtTree',RLT)
        RLTchecking(RLT)

    except Exception as err:
        print(err)

def searchLenghtInRLT(data , dataLength,_RLT):

    if _RLT is not None:
        if _RLT.data==dataLength:

            print("working here!",_RLT.info)
            if len(_RLT.info) == 0:
                _RLT.info.append(data)
                print("Data Inserted :", data)
            else:
                for i in _RLT.info:
                    if i == data:
                        print("Already Exit!")
                        return _RLT


                _RLT.info.append(data)
                print("Data Inserted :", data)



        if _RLT.data < dataLength :
            _RLT.right = searchLenghtInRLT(data , dataLength , _RLT.right)
        else:
            _RLT.left = searchLenghtInRLT(data , dataLength , _RLT.left)
    return _RLT

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


def searchingInDB(root, Oo, name):
    if root is not None:
        currentValue = ord(root.CharAlphbet)
        incomeValue = ord(Oo)

        print(currentValue, incomeValue)
        if currentValue == incomeValue:
            print("We Found Data",name,type(name))
            return name
            # work here

            # insertToRootLengthTree(name)

        elif currentValue < incomeValue:
            name1 =searchingInDB(root.c_right, Oo, name)
            return name1
        elif currentValue > incomeValue:
            name2 = searchingInDB(root.c_left, Oo, name)
            return name2

if __name__ == "__main__":
    root=dataInsertion()
    inorder(root)
    while True:
        name=input("Please enter name!")
        name = name.lower()

        Oo=name[0]

        flag = searching(root,Oo,name)

        


        
