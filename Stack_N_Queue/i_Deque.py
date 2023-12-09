'''
                  Assignment:- Deque Implementation Using List Concept

1. Define a class Deque to implement deque Data Structure using List Concept. 
2. Define __init__() method to create an empty list object as instance object member of deque.
3. Define a method is_empty() to check if the Deque is empty in Queue class.
4. In Deque class, define insert_front() method to add data at the front end of the deque.
5. In Deque class, define insert_rear() method to add data at the rear end of the deque.
6. In Deque class, define delete_front() method to remove front element from the deque.
7. In Deque class, define delete_rear() method to remove rear element from the deque.
8. In Deque class, define get_front() method to return front element of the deque.
9. In Deque class, define get_rear() method to return rear element of the deque.
10.In Deque class, define size() method to return size of the deque that is number of items
   present in the deque.

'''
class Deque:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==None
    def insert_front(self,data):
        self.items.insert(0,data)
    def insert_rear(self,data):
        self.items.append(data)
    def delete_front(self):
        if not self.is_empty():
          self.items.pop(0)
        else:
            raise IndexError('Deque is Empty')
    def delete_rear(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError('Deque is Empty')
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('Not Found')
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Not Found')
    def size(self):
        return len(self.items)

d=Deque()
d.insert_front(10)
d.insert_rear(20)
d.insert_rear(30)
d.insert_rear(40)
d.delete_front()
print(d.get_front())
d.delete_rear()
print(d.get_rear())
print(d.size())

