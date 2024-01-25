'''
                  Assignment 8:-- Stack Using Linked List Concept

            "(The Working Principle of Stack is LIFO - Last In First Out)"

1. Import module containing singly linked list code in your python file.

2. Define a class Stack to implement stack data structure.Define  __init__() method to create Singly
   Linked List(SLL) object.

3. Define a method is_empty() to check if the stack is empty in Stack class.

4. In stack class, define push() method to add data onto the stack.

5. In stack class, define pop() method to remove top element from the stack.

6. In stack class, define peek() method to return top element on the stack.

7. In stack class, define size() method to return size of the stack that is number of items
   present in the stack.

'''
from SLL import *


class Stack:
    def __init__(self):
        self.mylist = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.mylist.is_empty()

    def push(self, data):
        self.mylist.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.mylist.start.item
            self.mylist.delete_first()
            self.item_count -= 1
            return data
        else:
            raise IndexError('Stack is Empty')

    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item

    def size(self):
        return self.item_count


# Driver Code:-->
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print('Top Element is ', s1.peek())
print('Remove Element is ', s1.pop())
print('Top Element is ', s1.peek())
print('Size of the Stack is ', s1.size())
