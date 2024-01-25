'''
                  Assignment:- Deque Implementation Using List Concept

1. Define a Class Node with instance object member variables prev,item and next.

2. Define a class Deque to implement deque Data Structure using Linked List Concept.

3. Define __init__() method to initialise front and rear reference variable and item_count variable
   to keep track of number of element in deque.

4. Define a method is_empty() to check if the Deque is empty in Queue class.

5. In Deque class, define insert_front() method to add data at the front end of the deque.

6. In Deque class, define insert_rear() method to add data at the rear end of the deque.

7. In Deque class, define delete_front() method to remove front element from the deque.

8. In Deque class, define delete_rear() method to remove rear element from the deque.

9. In Deque class, define get_front() method to return front element of the deque.

10. In Deque class, define get_rear() method to return rear element of the deque.

11.In Deque class, define size() method to return size of the deque that is number of items
   present in the deque.

'''


class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.front == None

    def insert_front(self, data):
        n = Node(None, data, self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count += 1

    def insert_rear(self, data):
        n = Node(self.rear, data, None)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1

    def delete_front(self):
        if self.is_empty():
            raise IndexError('Deque is Empty')
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError('Deque is Empty')
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError('Deque is Empty')
        return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError('Deque is Empty')
        return self.rear.item

    def size(self):
        return self.item_count


d = Deque()
d.insert_front(10)
d.insert_front(20)
d.insert_rear(30)
d.insert_rear(40)
print('First Element of Deque is ', d.get_front())
d.delete_front()
print('First Element of Deque is ', d.get_front())
# d.delete_rear()
print('Last Element of Deque is ', d.get_rear())
print('No. of Element in Deque is', d.size())
