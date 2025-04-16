class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <-> '
            temp_node = temp_node.next
        return result

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def reverse_traversal(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    def search(self, target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def get(self, index):
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index , -1):
                current_node = current_node.prev
        return current_node

    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index ,value):
        if index < 0 or index > self.length:
            print("Index out of bounds..")
            return
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        temp_node = self.get(index - 1)
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1

    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
            return popped_node
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
            self.length -= 1
        return popped_node.value

    def pop_last(self):
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
            return popped_node
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node.value

    def remove(self,index):
        popped_node = self.get(index)
        if self.length == 1:
            self.head = self.tail = 0
            self.length = 0
        else:
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
            popped_node.prev = popped_node.next = 0
            self.length -= 1
        return popped_node



newDLL = DoubleLinkedList()
newDLL.append(1)
newDLL.append(2)
newDLL.prepend(3)
newDLL.reverse_traversal()
print(newDLL.search(1))
newDLL.set_value(0, 6)
newDLL.insert(3,99)

# print(newDLL.pop_first())
# print(newDLL.pop_last())
print(newDLL.remove(1))


print(newDLL.__str__())
# print(newDLL.get(0))
# print(newDLL.head.value)
# print(newDLL.head.next.value)
# print(newDLL.__str__())