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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1



new_cdll = CircularDoubleLL(10)
print(new_cdll.length)