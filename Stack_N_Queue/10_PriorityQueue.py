'''
                          Assignment :- Priority Queue Using list

1. Define a Class PriorityQueue to implement priority queue data structure using list.

2. Define __init__() method to create a list object(initially empty).

3. Define a push method in Priority Queue Class to insert new data with given priority.

4. Define a pop method in Priority Queue Class,which return the highest priority data 
   store in the priority queue data structure.Raise exception if priority queue is empty.

5. Define is_empty() method in priority queue class to check if the priority queue is empty.

6. In class Priority Queue,define a method size to return the number of elements present
   in the priority queue.

'''
class PriorityQueue:
    def __init__(self):
        self.items=[]
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if not self.is_empty():
           return self.items.pop(0)[0]
    def size(self):
        return len(self.items)

# Driver Code:

p=PriorityQueue()
p.push(10,8)
p.push(20,1)
p.push(30,3)
p.push(40,6)
p.push(50,5)

print('Size of the PriorityQueue is ',p.size())

while not p.is_empty():
  print('Highest Priority number is ',p.pop())
