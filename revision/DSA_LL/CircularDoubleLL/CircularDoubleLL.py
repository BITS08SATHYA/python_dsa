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

    def __str__(self):
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head: break
            result += ' <-> '
        return result



new_cdll = CircularDoubleLL()
new_cdll.append(10)
new_cdll.append(20)
print(new_cdll.__str__())
# print(new_cdll.head.value)
# print(new_cdll.head.next.value)