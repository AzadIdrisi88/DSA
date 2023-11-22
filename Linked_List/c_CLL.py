'''
circular Linked list is a linear data structure.
                          Assignment 3-:- Circular Linked List
1. Define a class Node to describe a node of a Circular Linked List.
2. Define a class CLL to implement Circular Linked list with __init__() method to create and initialise
   start reference variable.
3. Define a method is_empty() to check if the linked list is empty in CLL class.
4. In class CLL, define a method insert_at_start() to insert an element at the starting of the list.
5. In class CLL, define a method insert_at_last() to insert an element at the end of the list.
6. In class CLL, define a method search() to find a node with specified element value.
7. In class CLL, define a method insert_after() to insert a new node after a given node of the list.
8. In class CLL, define a method to print all the elements of the list.
9. In class CLL, implement Iterator for CLL to access all the elements of the list in a sequence.
10.In class CLL, define a method  delete_first() to delete first element from the list.
11.In class CLL, define a method  delete_last() to delete last element from the list.
10.In class CLL, define a method  delete_item() to delete specified element from the list.

'''


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class CLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last == None

    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n

    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            n.next = self.last.next
            self.last.next = n
            self.last = n

        else:
            n.next = n
            self.last = n

    def search(self, data):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
            if temp == self.last:
                self.last = n

    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=' ')
                temp = temp.next
            print(temp.item)

    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_item(self, data):
        if not self.is_empty():
            if self.last.next == self.last:
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item == data:
                    self.delete_first()
                else:
                    temp = self.last.next
                    while temp != self.last:
                        if temp.next == self.last:
                            if self.last.item == data:
                                self.delete_last()
                                break
                        if temp.next.item == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next

    def __iter__(self):
        if self.last == None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)


class CLLIterator:
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


# Driver Code
mylist = CLL()
mylist.insert_at_start(48)
mylist.insert_at_start(98)
mylist.insert_at_last(100)
mylist.insert_at_last(120)
mylist.insert_after(mylist.search(98), 99)
mylist.print_list()

# mylist.delete_first()
# mylist.delete_last()
# mylist.delete_item(10)
# mylist.print_list()


for i in mylist:
    print(i, end=' ')
