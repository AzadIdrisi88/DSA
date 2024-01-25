'''
                 Assignment 8:-- Stack Implementation by extending SLL

            "(The Working Principle of Stack is LIFO - Last In First Out)"

1. Import module containing singly linked list code in your python file.

2. Define a class Stack to implement stack data structure by inheriting SLL class.

3. Define a method is_empty() to check if the stack is empty in Stack class.

4. In stack class, define push() method to add data onto the stack.

5. In stack class, define pop() method to remove top element from the stack.

6. In stack class, define peek() method to return top element on the stack.

7. In stack class, define size() method to return size of the stack that is number of items
   present in the stack.

'''
from SLL import *


class Stack(SLL):
    def __init__(self):
        self.item_count = 0
        super().__init__()

    def is_empty(self):
        return super().is_empty()

    def push(self, data):
        self.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.delete_first()
            self.item_count -= 1
            return data
        else:
            raise IndexError('Stack Uderflow')

    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('stack is Empty')

    def size(self):
        return self.item_count


# Driver Code:-->
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print('Top Element is ', s.peek())
print('Remove Element is ', s.pop())
print('Top Element is ', s.peek())
print('Remove Element is ', s.pop())
print('Top Element is ', s.peek())
print("Size of the Stack is ", s.size())
