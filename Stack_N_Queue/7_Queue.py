'''                 Assignment 2:- Queue Using Singly Linked List Concept

                "(The Working Principle of Queue is FIFO - First In First Out)"

1. Define a class Queue to implement Queue Data Structure using Singly Linked List Concept.

2. Define __init__() method to initialise front and rear reference variable and item_count variable 
   to keep track of number of element in a queue.

3. Define a method is_empty() to check if the Queue is empty in Queue class.

4. In Queue class, define enqueue() method to add data at the rear end of the queue.

5. In Queue class, define dequeue() method to remove front element from the queue.

6. In Queue class, define get_front() method to return front element of the queue.

7. In Queue class, define get_rear() method to return rear element of the queue.

8. In Queue class, define size() method to return size of the queue that is number of items
   present in the queue.
'''


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.front == None

    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Empty Queue')
        elif self.front == self.rear:
            data = self.front.item
            self.front = None
            self.rear = None
        else:
            data = self.front.item
            self.front = self.front.next
            self.item_count -= 1
        return data

    def get_front(self):
        if self.is_empty():
            raise IndexError('No data in the Queue')
        else:
            return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError('No data in the Queue')
        else:
            return self.rear.item

    def size(self):
        return self.item_count


# Driver Code:-->
q = Queue()
q.enqueue(10)
q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
print('Front value of the Queue is ', q.get_front())
# print('Rear value of the Queue is ', q.get_rear())
print('Remove element from Queue is ', q.dequeue())
print('Front value of the Queue is ', q.get_front())
print('Size of the Queue = ', q.size())
