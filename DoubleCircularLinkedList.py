class Node:

    def __init__(self,data=None) -> None:
        self.previous = None
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)

class DoubleCircularLinkedList:

    def __init__(self) -> None:
        self.head = Node()

    def append(self,data):
        node = Node(data)
        if self.head.data == None:
            self.head = node
            self.head.previous = self.head
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            previous = current
            node.previous = previous
            node.next = self.head
            current.next = node
            self.head.previous = node

    def appendleft(self,data):
        node = Node(data)
        node.previous = self.head.previous
        node.next = self.head
        self.head.previous.next = node
        self.head.previous = node
        self.head = node

    def traversal(self):
        current = self.head
        while current.next != self.head:
            print("========================")
            print("Previous ",current.previous) 
            print("Current ",current)
            print("Next ",current.next)
            print("========================")
            current = current.next
        print("========================")
        print("Previous ",current.previous) 
        print("Current ",current)
        print("Next ",current.next)
        print("========================")

dcll = DoubleCircularLinkedList()
dcll.append("10")
dcll.append("20")
dcll.append("30")
dcll.appendleft("5")
dcll.traversal()
