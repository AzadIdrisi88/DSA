'''
                          Assignment 2-:- Doubly Linked List
                          
1. Define a class Node to describe a node of a Doubly Linked List.
2. Define a class DLL to implement Doubly Linked list with __init__() method to create and initialise
   start reference variable.
3. Define a method is_empty() to check if the linked list is empty in DLL class.
4. In class DLL, define a method insert_at_start() to insert an element at the starting of the list.
5. In class DLL, define a method insert_at_last() to insert an element at the end of the list.
6. In class DLL, define a method search() to find a node with specified element value.
7. In class DLL, define a method insert_after() to insert a new node after a given node of the list.
8. In class DLL, define a method to print all the elements of the list.
9. In class DLL, implement Iterator for DLL to access all the elements of the list in a sequence.
10.In class DLL, define a method  delete_first() to delete first element from the list.
11.In class DLL, define a method  delete_last() to delete last element from the list.
10.In class DLL, define a method  delete_item() to delete specified element from the list.


'''
class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        temp = self.start
        if self.start != None:
            while temp.next != None:
                temp = temp.next
        n = Node(temp, data, None)
        if temp == None:
            self.start = n
        else:
            temp.next = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    def print_list(self):
        # result=[]
        temp = self.start
        while temp is not None:
            # result.append(temp.item)
            print(temp.item, end=' ')
            temp = temp.next
        # return result
        print()

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_item(self, data):
        if self.start is None:
            pass
        temp = self.start
        while temp is not None:
            if temp.item == data:
                if temp.next is not None:
                    temp.next.prev = temp.prev
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.start = temp.next
                    break
            temp = temp.next

    def __iter__(self):
        return DLLiterator(self.start)


class DLLiterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# # driver code
# mylist = DLL()
# mylist.insert_at_start(25)
# mylist.insert_at_last(88)
# mylist.insert_after(mylist.search(25), 78)
# # print(mylist.print_list())

# mylist.delete_item(78)
# mylist.print_list()

# # mylist.delete_first()
# # print(mylist.print_list())

# # mylist.delete_last()
# # print(mylist.print_list())

# # for x in mylist:
# #     print(x, end=' ')
