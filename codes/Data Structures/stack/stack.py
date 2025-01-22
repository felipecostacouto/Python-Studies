class Stack:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class stk:

    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def __repr__(self):
        items = []
        current_item = self.top

        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next

        return '->'.join(items)

    def push(self, value):
        new_val = Stack(value)
        new_val.next = self.top
        self.top = new_val

        self.size += 1

    def pop(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        
        pop_value = self.top.value
        self.top = self.top.next

        self.size -= 1
        
        return pop_value

    def peek(self):
        if self.top is None:
            raise ValueError("Stack is Empty")
        return self.top.value

    def is_empty(self):
        return self.top is None


if __name__ == '__main__':
    stack = stk()

    stack.push(10)
    stack.push(14)
    stack.push(16)
    stack.push(6)
    stack.push(12)

    print(stack)

    print(stack.peek())

    print(stack.pop())
    print(stack)