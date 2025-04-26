# import queue as q
from collections import deque as Queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
# print(newBT.data)
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
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

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.append(rootNode)
        while not(len(customQueue) == 0):
            root = customQueue.popleft()
            print(root.data)
            if root.leftChild is not None:
                customQueue.append(root.leftChild)
            if root.rightChild is not None:
                customQueue.append(root.rightChild)

print('PreOrder Traversal')
print('-----------------')
preOrderTraversal(newBT)
print('\n')
print('InOrder')
print('-----------------')
inOrderTraversal(newBT)
print('\n')
print('PostOrder')
print('-----------------')
postOrderTraversal(newBT)
print('\n')
print('LevelOrder')
print('-----------------')
levelOrderTraversal(newBT)