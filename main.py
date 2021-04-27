#Using the above examples as a guide, create your own interpretation of the a Linked List class. 
#You can not use the code above exactly, but again it can be used as a guide. 

class Node:
    def __init__(self, dataval= None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headvalue = None

# Print the linked list
    def listprint(self):
        printvalue = self.headval
        while printvalue is not None:
            print (printvalue.datavalue)
            printval = printvalue.nextvalue
    def AtBegining(self,newdata):
        NewNode = Node(newdata)

# Update the new nodes next val to existing node
        NewNode.nextvalue = self.headvalue
        self.headvalue = NewNode

list = LinkedList()
list.headvalue = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headvalue.nextvalue = e2
e2.nextvalue = e3

list.AtBegining("Sun")

list.listprint()

#Using the above examples as a guide, create your own interpretation of the a Binary Search Tree class. 
#You can not use the code above exactly, but again it can be used as a guide.

class TreeNode():
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def BST(root):
    forest = []
    prev = None
    
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and root.value <= prev.value:
            return False
        prev = root
        root = root.right
    return True

root = TreeNode(2)  
root.left = TreeNode(1)  
root.right = TreeNode(3) 
 
result = BST(root)
print(result)

root = TreeNode(1)  
root.left = TreeNode(2)  
root.right = TreeNode(3) 
 
result = BST(root)
print(result)
