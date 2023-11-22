'''
Stack is also a linear data structure.Data Structure is like a container in which we store data.
                             
                          Assignment 5:-- Stack Using List

1. Define a class Stack to implement stack data structure using list.
   Define __init__() method to create an empty list object as instance object member of stack.
2. Define a method is_empty() to check if the stack is empty in Stack class.
3. In stack class, define push() method to add data onto the stack.
4. In stack class, define pop() method to remove top element from the stack.
5. In stack class, define peek() method to return top element on the stack.
6. In stack class, define size() method to return size of the stack that is number of items
   present in the stack.

'''


class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0

    def push(self, data):
        self.item.append(data)

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Stack is Empty")

    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Stack is Empty")

    def size(self):
        return len(self.item)

# Driver Code -->


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
print('Top element is ',s1.peek())
# print('Remove element is ', s1.pop())
# print('Top element is ',s1.peek())
print('Size of the list ', s1.size())
