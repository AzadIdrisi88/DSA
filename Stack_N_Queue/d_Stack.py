'''
                            Assignment 7:-- Stack Using Linked List Concept

                   "(The Working Principle of Stack is LIFO - Last In First Out)"

1. Define a class Stack to implement stack data structure using singly linked list concept.
2. Define  __init__() method to initialise start reference variable and item_count variable
   to keep track of number of elements in the stack.
3. Define a method is_empty() to check if the stack is empty in Stack class.
4. In stack class, define push() method to add data onto the stack.
5. In stack class, define pop() method to remove top element from the stack.
6. In stack class, define peek() method to return top element on the stack.
7. In stack class, define size() method to return size of the stack that is number of items
   present in the stack.
   
'''
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Stack:
    def __init__(self):
        self.top=None
        self.item_count=0
    def is_empty(self):
        return self.top==None
    def push(self,data):
        n=Node(data,self.top)
        self.top=n
        self.item_count +=1
    def pop(self):
        if not self.is_empty():
           data=self.top.item
           self.top=self.top.next
           self.item_count-=1
           return data
        else:
            raise IndexError('Stack is Empty')
    def peek(self):
        if not self.is_empty():
            return self.top.item
        else:
            raise IndexError('stack is empty')
    def size(self):
        return self.item_count
# Driver Code :
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print('Top element of the list ',s1.peek())
# print('Remove the last element ',s1.pop())
# print('Top element of the list ',s1.peek())
print('No of element in Stack ',s1.size())




