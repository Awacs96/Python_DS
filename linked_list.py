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
    
    def print_list(self):
        itr = self.head

        while itr:
            print(itr.value)
            itr = itr.next
    

ll = LinkedList(Node(3))
ll.append(Node(4))
ll.print_list()