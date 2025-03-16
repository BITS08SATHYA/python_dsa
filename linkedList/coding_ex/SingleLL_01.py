class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def append(self,value):
        new_node = Node(value)
        if self.tail is None and self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            popped_node = self.head
            if self.head == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next

            popped_node = temp.next

            if popped_node.next is None:
                self.tail = temp

            temp.next = temp.next.next
            popped_node.next = None
            self.length -= 1
            return popped_node