class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linked_list:

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, value):
        new_node = Node(value)
        