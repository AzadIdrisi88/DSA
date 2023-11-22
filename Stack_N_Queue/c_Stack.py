'''
                        Assignment 6:-- Stack Extending List

1. Define a class Stack to implement stack data structure by extending list class.
2. Define a method is_empty() to check if the stack is empty in Stack class.
3. In stack class, define push() method to add data onto the stack.
4. In stack class, define pop() method to remove top element from the stack.
5. In stack class, define peek() method to return top element on the stack.
6. In stack class, define size() method to return size of the stack that is number of items
   present in the stack.
7. Implement a way to restrict use of insert() method of list class from stack object.


'''
class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
          return super().pop()
        else:
            raise IndexError('Stack is Empty')
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('Stack is Empty')
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("No attribute 'insert' in Stack")
    
# Driver Code :-->

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print('Top element of the list ',s1.peek())
print('Remove element from the list',s1.pop())
print('Top element of the list ',s1.peek())
print(s1.count(10))
print('size of the list',s1.size())
        
