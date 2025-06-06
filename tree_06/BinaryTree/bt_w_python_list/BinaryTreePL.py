class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex+1 == self.maxSize:
            return "The Binary Tree is Full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return f"The value {value} has been inserted"

    def searchNode(self, nodevalue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodevalue:
                return "Success"
        return "Not Found"

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been deleted"
        return "Not Found"

    def deleteBT(self):
        self.customList = None
        return "The binary tree has been deleted"


newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
# print(newBT.searchNode("Hot"))

# # PreOrder Traversal
# # Root Node --> Left Subtree --> Right Subtree
# print("PreOrder Traversal")
# newBT.preOrderTraversal(1)
#
# # InOrder Traversal
# # Left Subtree --> Root Node --> Right Subtree
# print("InOrder Traversal")
# newBT.inOrderTraversal(1)
# # Post Traversal
# # Left Subtree --> Right Subtree --> Root node
# print("PostOrder Traversal")
# newBT.postOrderTraversal(1)
#
# # Level Order traversal
# print("Level Order Traversal")
# newBT.levelOrderTraversal(1)

print(newBT.deleteNode("Tea"))
print("Level Order Traversal")
newBT.levelOrderTraversal(1)