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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            new_node.prev = new_node
            new_node.next = new_node
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.head = new_node
        self.length += 1

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break

    def reverse_traverse(self):
        curr_node = self.tail
        while curr_node:
            print(curr_node.value)
            curr_node = curr_node.prev
            if curr_node == self.tail:
                break

    def search(self, target):
        curr_node = self.head
        while curr_node:
            if curr_node.value == target:
                return True
            curr_node = curr_node.next
            if curr_node == self.head:
                break
        return False

    def get(self, index):
        curr_node = None
        if index < self.length // 2:
            curr_node = self.head
            for _ in range(index):
                curr_node = curr_node.next
        else:
            curr_node = self.tail
            for _ in range(self.length-1, index, -1):
                curr_node = curr_node.prev
        return curr_node

    def set(self, index, value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Error: Index out of bounds")
            return
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return
        new_node = Node(value)
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
        self.head = self.head.next
        popped_node.prev = None
        popped_node.next = None
        self.head.prev = self.tail
        self.tail.next = self.head
        self.length -= 1
        return popped_node

    def pop_last(self):
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
            return popped_node
        self.tail = self.tail.prev
        popped_node.prev = None
        popped_node.next = None
        self.head.prev = self.tail
        self.tail.next = self.head
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop_last()
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.prev = None
        popped_node.next = None
        self.length -= 1
        return popped_node




new_cdll = CircularDoubleLL()
new_cdll.append(10)
new_cdll.append(20)
new_cdll.prepend(30)
new_cdll.insert(1,99)
# print(new_cdll.get(0))
print(new_cdll.__str__())
# print(new_cdll.traverse())
# print(new_cdll.reverse_traverse())
# print(new_cdll.head.value)
# print(new_cdll.head.next.value)