'''
                          Assignment :- Priority Queue Using Linked List

1. Define a Node Class with instance member variables item,priority and next.

2. Define a class PriorityQueue to implement priority queue data structure using singly linked list.
   Define __init__() method to create a start reference variable(initially containing None) and 
   item_count variable(initially 0).

3. Define a push method in Priority Queue Class to insert new data with given priority.

4. Define a pop method in Priority Queue Class,which return the highest priority data 
   store in the priority queue data structure.Raise exception if priority queue is empty.

5. Define is_empty() method in priority queue class to check if the priority queue is empty.

6. In class Priority Queue,define a method size to return the number of elements present
   in the priority queue.

'''


class Node:
    def __init__(self, item=None, priority=None, next=None):
        self.item = item
        self.priority = priority
        self.next = next


class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None

    def push(self, data, priority):
        n = Node(data, priority)
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('PriorityQueue is Empty')
        else:
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
        return data

    def size(self):
        return self.item_count


p = PriorityQueue()
p.push(10, 2)
p.push(80, 3)
p.push(85, 1)
p.push(70, 7)
p.push(90, 5)
p.push(40, 6)

# while not p.is_empty():
print(p.pop())
print(p.size())
