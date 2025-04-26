class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
# print(newBT.data)
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

print('PreOrder Traversal')
print('-----------------')
preOrderTraversal(newBT)
print('\n')
print('InOrder')
print('-----------------')
inOrderTraversal(newBT)