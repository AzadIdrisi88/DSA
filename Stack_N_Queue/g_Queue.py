'''
                    Assignment 1:- Queue Using List

        "(The Working Principle of Queue is FIFO - First In First Out)"
        
1. Define a class Queue to implement Queue Data Structure using list. 
2. Define __init__() method to create an empty list object as instant object member of Queue.
3. Define a method is_empty() to check if the Queue is empty in Queue class.
4. In Queue class, define enqueue() method to add data at the rear end of the queue.
5. In Queue class, define dequeue() method to remove front element from the queue.
6. In Queue class, define get_front() method to return front element of the queue.
7. In Queue class, define get_rear() method to return rear element of the queue.
8. In Queue class, define size() method to return size of the queue that is number of items
   present in the queue.
'''


class Queue:
    def __init__(self):
        self.mylist = []
        pass

    def is_empty(self):
        return len(self.mylist) == 0

    def enqueue(self, data):
        self.mylist.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.mylist.pop(0)
        else:
            raise IndexError('Queue underflow')

    def get_front(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            raise IndexError('Queue underflow')

    def get_rear(self):
        if not self.is_empty():
            return self.mylist[-1]
        else:
            raise IndexError('Queue underflow')

    def size(self):
        return len(self.mylist)


# Driver Code:-->
q1 = Queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print('Front Element is ', q1.get_front())
try:
    print('Remove Element is ', q1.dequeue())
    print('Queue has Now ', q1.size(), ' elements')
except IndexError as e:
    print(e.args[0])
# print('Front Element is ', q1.get_front())
print('Rear Element is ', q1.get_rear())
print('Size of the Queue is ', q1.size())
