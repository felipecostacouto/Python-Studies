class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def __repr__(self):
        items = []
        current_item = self.front

        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next

        return ', '.join(items)

    def enqueue(self, value):
        new_node = Node(value)
        
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def dequeue(self):
        if self.front is None:
            raise IndexError('Queue is empty')
        
        dequeue_value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1
        
        return dequeue_value

    def peek(self):
        if self.front is None:
            raise IndexError('Queue is empty')
        
        return self.front.value

    def is_empty(self):
        return self.front is None

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.enqueue(60)

    print(queue)
    print(len(queue))

    print(queue.dequeue())

    print(queue)