'''
Doubly Circular LLinked List is also linear data structure.
                              Assignment 4-:- Circular Doubly Linked List
1. Define a class Node to describe a node of a Circular Doubly Linked List.
2. Define a class CDLL to implement Circular Doubly Linked list with __init__() method to create and initialise
   start reference variable.
3. Define a method is_empty() to check if the linked list is empty in CLL class.
4. In class CDLL, define a method insert_at_start() to insert an element at the starting of the list.
5. In class CDLL, define a method insert_at_last() to insert an element at the end of the list.
6. In class CDLL, define a method search() to find a node with specified element value.
7. In class CDLL, define a method insert_after() to insert a new node after a given node of the list.
8. In class CDLL, define a method to print all the elements of the list.
9. In class CDLL, implement Iterator for CDLL to access all the elements of the list in a sequence.
10.In class CDLL, define a method  delete_first() to delete first element from the list.
11.In class CDLL, define a method  delete_last() to delete last element from the list.
10.In class CDLL, define a method  delete_item() to delete specified element from the list.

'''


class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class CDLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            n.prev.next = n
            self.start.prev = n

    def search(self, data):
        temp = self.start
        if temp == None:
            return None
        if temp.item == data:
            return temp
        else:
            temp = temp.next
        while temp != self.start:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(item=data)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n

    def print_list(self):
        temp = self.start
        if temp is None:
            return
        print(temp.item, end=' ')
        temp = temp.next
        while temp is not self.start:
            print(temp.item, end=' ')
            temp = temp.next

    def delete_first(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next

    def delete_last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev

    def delete_item(self, data):
        if self.start is not None:
            temp = self.start
            if temp.item == data:
                self.delete_first()
            else:
                temp = temp.next
                while temp != self.start:
                    if temp.item == data:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                        break
                    temp = temp.next

    def __iter__(self):
        return CDLLIterator(self.start)


class CDLLIterator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current = self.current.next
        return data


# Driver Code :->
mylist = CDLL()
mylist.insert_at_start(50)
mylist.insert_at_start(40)
mylist.insert_at_last(60)
mylist.insert_after(mylist.search(60), 70)
# mylist.print_list()

# mylist.delete_first()
# mylist.delete_last()
# mylist.delete_item(44)

mylist.print_list()

# for x in mylist:
#     print(x,end=' ')
