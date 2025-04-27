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

newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
# print(newBT.searchNode("Hot"))

# PreOrder Traversal
# Root Node --> Left Subtree --> Right Subtree
newBT.preOrderTraversal(1)

# InOrder Traversal
# Left Subtree --> Root Node --> Right Subtree

# Post Traversal

# Level Order traversal
