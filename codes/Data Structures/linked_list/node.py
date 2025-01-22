class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def  __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head

            return_string = f"[{last.value}"

            while last.next:
                last = last.next
                return_string += f", {last.value}"
            return_string += "]"

            return return_string


    def __contains__(self, value):
        last = self.head

        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter

    # O(n)
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)
            
    # O(1) - constant time
    def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node

    # O(n) - linear time
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head

                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next
                
                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node

    def delete(self, value):
        last = self.head

        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        last.next = last.next.next
                        break
                    last = last.next

    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head

            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next

            if last.next is None:
                    raise ValueError("Index out of bounds")
            else:
                last.next = last.next.next
                

    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            return last.value

    def print(self):
        pass

if __name__ == "__main__":
    ll = LinkedList()

    ll.append(10)
    ll.append(5)
    ll.append(18)
    ll.append(22)
    ll.append(28)

    ll.prepend(100)

    ll.insert(200, 1)

    ll.pop(1)
    print(ll)



         