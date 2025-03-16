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

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    def remove_duplicates(self):
        if self.head is None:
            return None
        node_values = set()  # set to store unique values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node =  current_node.next
        self.tail = current_node

