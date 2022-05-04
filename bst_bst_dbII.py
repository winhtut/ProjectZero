
class LenghtBST:
    def __init__(self,data):
        self.data=data
        self.info=[]
        self.infoPw=[]
        self.left=None
        self.right=None

class LengthData:
    def __init__(self):
        self.root = None

    def storeLengthTree(self):
        list_length=[16,8,24,4,12,20,28,2,6,10,14,18,22,26,29,1,3,5,7,9,11,13,15,17,19,21,23,25,27,30]
        length=len(list_length)
        print(length)

        for i in range(0,length):
            print("data",list_length[i])
            self.root = insert(self.root,list_length[i])

        return self.root

def insert(node, key):

    # Return a new node if the tree is empty
    if node is None:
        return LenghtBST(key)
    # Traverse to the right place and insert the node
    if key < node.data:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

# if __name__=="__main__":
#     obj = LengthData()
#     root =obj.storeLengthTree()
#     print(root)

root_length_tree = LengthData()
root_lenght_tree_info=LenghtBST('data')