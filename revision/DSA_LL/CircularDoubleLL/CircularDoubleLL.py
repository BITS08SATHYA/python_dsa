class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

    # def __init__(self,value):
    #     new_node = Node(value)
    #     new_node.prev = new_node
    #     new_node.next = new_node
    #     self.head = self.tail = new_node
    #     self.length = 1


class CircularDoubleLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0



new_cdll = CircularDoubleLL(10)
print(new_cdll.length)