# Linked List

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, node):
        self.head = node
    
    def append(self, node):
        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = node
    
    # Next steps:
    # remove from certain index
    # remove certain value
    # get length of the list
    # insert on certain position
    # 
    
    def print_list(self):
        itr = self.head
        lst = ""

        while itr:
            lst += str(itr.value)
            lst += " -> "
            itr = itr.next

        lst = lst[:-4]
        print(lst)

ll = LinkedList(Node(3))
ll.append(Node(4))
ll.append(Node(5))
ll.print_list()