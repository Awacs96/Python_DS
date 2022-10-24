class Node:

    def __init__(self, value):
        self.value = value
        self.next=None
        self.prev=None
    
class DoublyLinkedList:

    def __init__(self):
        self.head = None
    
    def append(self, node):
        
        if self.head:
            itr = self.head

            while itr.next:
                itr = itr.next
            
            itr.next = node
            itr.next.prev = itr
        else:
            self.head = node
    
    def print(self):

        if self.head:
            itr = self.head

            while itr:
                if itr.next:
                    print(f"Node value: {itr.value}. Previous node: {itr.prev.value if itr.prev else None}. Next node: {itr.next.value}")
                else:
                    print(f"Node value: {itr.value}. Previous node: {itr.prev.value if itr.prev else None}. Next node: {None}")
                itr = itr.next
        else:
            print("List is empty.")


item1 = Node(5)
item2 = Node(8)
item3 = Node(1)

dll = DoublyLinkedList()
dll.print()
dll.append(item1)
dll.append(item2)
dll.append(item3)
dll.print()
