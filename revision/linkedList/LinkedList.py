class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# class LinkedList:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
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

    def search(self, target):
        curr = self.head
        index = 0
        while curr is not None:
            if curr.value == target:
                # return True
                return index
            curr = curr.next
            index += 1
        return -1

    def get(self, index):
        if index == -1:
            return self.tail.value
        if index < 0 or index >= self.length:
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    def set(self, index, value):
        if index == -1:
            return self.tail.value
        if index < 0 or index >= self.length:
            return None
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result




new_linked_list = LinkedList()
new_linked_list.append(1)
new_linked_list.append(2)
new_linked_list.prepend(3)
new_linked_list.insert(2, 5)
print(new_linked_list.__str__())
# new_linked_list.traverse()
# print(new_linked_list.search(1))
print(new_linked_list.get(3))
# print(new_linked_list.head.value)
# print(new_linked_list.head.next.value)