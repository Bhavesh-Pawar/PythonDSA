class Node:
    def __init__(self,data=None) -> None:
        self.previous = None
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return str(self.data)

class DLL:

    def __init__(self) -> None:
        self.head = Node()

    def append(self,data):
        node = Node(data)
        if self.head.data == None:
            self.head = node
        else:
            current = self.head 
            previous = self.head
            while current.next != None:
                current = current.next
                previous = current
            current.next = node
            node.previous = previous

    def appendleft(self,data):
        node = Node(data)
        node.next = self.head
        self.head.previous = node
        self.head = node

    def insert_after(self,data,new_data):
        node = Node(new_data)
        temp = self.head
        while temp.data != data:
            temp = temp.next
            if temp == None:
                print("Data Not Found")
                return
        next_node = temp.next
        node.next = next_node
        next_node.previous = node
        temp.next = node
        node.previous = temp


    def deletelast(self):
        temp = self.head
        previous = temp
        while temp.next != None:
            previous = temp 
            temp = temp.next
        previous.next = None

    def deletefirst(self):
        temp = self.head
        temp.next.previous = None
        self.head = temp.next

    def delete_data(self,data):
        temp = self.head
        while temp.data != data:
            temp = temp.next
            if temp == None:
                print("Data Not Found")
                return
        previous = temp.previous 
        previous.next = temp.next
        temp.next.previous = previous
        
    def traversal(self):
        current = self.head

        while current != None:
            print("Previous ",current.previous)
            print("Current ",current.data)
            print("Next ",current.next)
            current = current.next


dll = DLL()
dll.append("10")
dll.append("20")
dll.append("30")
# dll.appendleft("5")
# dll.appendleft("2")
# dll.append("5")
# dll.append("2")
# dll.deletelast()
# dll.deletelast()
# dll.deletefirst()
# dll.deletefirst()
# dll.insert_after("15","25")
dll.delete_data("20")
dll.traversal()
