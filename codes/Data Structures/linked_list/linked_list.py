class linked_list:
    def __init__(self, data):
        self.data = data
        self.next = None

    def insertAtBegin(self, data):
        new_node = linked_list(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)

        position = 0
        current_node = self.head
        while current_node != None and position+1 != index:
            position = position + 1
            current_node = current_node.next
        
        if current_node != None:
            new_node = linked_list(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")
    

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to the next node

# LinkedList class manages the nodes and operations of the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
'''