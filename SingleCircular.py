class Node:
    def __init__(self,data=None) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)

class SingleCircularLL:
    
    def __init__(self) -> None:
        self.head = Node()

    def append(self,data):

        node = Node(data)
        if not self.head.data  :
            self.head = node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
        node.next = self.head

    def appendleft(self,data):
        node = Node(data)
        temp = self.head
        node.next = temp
        # self.head = node
        while temp.next != self.head:
            temp = temp.next
        
        temp.next = node
        self.head = node

    def traversal(self):
        temp = self.head
        while temp.next != self.head:
            print(temp.data)
            # print("Current ",temp.data)
            # print("Next ",temp.next.data)
            temp = temp.next
        print(temp.data)
        # print("Current ",temp.data)
        # print("Next ",temp.next.data)
circular_list = SingleCircularLL()
circular_list.append("10")
circular_list.append("20")
circular_list.append("30")
circular_list.appendleft("5")
circular_list.traversal()
