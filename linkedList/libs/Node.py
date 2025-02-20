class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self) -> str:
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index ,value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end = "->")
            current_node = current_node.next
        print("Null")

    def search(self, value):
        temp_node = self.head
        index = 0
        while temp_node:
            if temp_node.value == value:
                return index
            temp_node = temp_node.next
            index = index + 1
        return -1

    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        elif self.length == 1 or index == 0:
            return self.head.value
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node.value

    def remove_all(self):
        self.head = self.tail = None
        self.length = 0



new_linked_list = LinkedList()
new_linked_list.append(1)
new_linked_list.prepend(4)
new_linked_list.append(2)
new_linked_list.append(3)
new_linked_list.insert(2,5)
# new_linked_list.pop()
# print(new_linked_list.head.value)
# print(new_linked_list.__str__())
new_linked_list.traverse()

# print(new_linked_list.remove(3))
new_linked_list.remove_all()
new_linked_list.traverse()
# print(new_linked_list.search(5))
# print(new_linked_list.get(2))
