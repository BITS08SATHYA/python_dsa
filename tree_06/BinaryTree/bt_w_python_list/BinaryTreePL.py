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

newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Coffee"))
print(newBT.searchNode("Hot"))
