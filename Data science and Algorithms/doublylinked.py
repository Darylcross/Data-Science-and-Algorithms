class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newNode
            newNode.prev=current
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_reverse(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

# Kullanım örneği:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

print("Doubly Linked List:")
dll.display()

#print("Doubly Linked List (Reverse):")
#dll.display_reverse()
print(self.2.next)