class Node:
    def __init__(self,data=None) -> None:
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return str(self.data)

class SingleLL:
    def __init__(self) -> None:
        self.head = Node()

    def append(self,data):
        node = Node(data)
        if self.head.data == None:
            self.head = node
        else:

            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
        
    def appendleft(self,data):
        node = Node(data)
        temp = self.head
        self.head = node
        self.head.next = temp

    def insert_after(self,data,new_data):
        node = Node(new_data)
        current = self.head
        while current.data != data:
            current = current.next
            if current == None:
                return "Data not found"
        temp = current.next
        current.data = data
        current.next = node
        node.next = temp
        return 1


    def delete_last(self):
        print("Deleting Last Element=============")
        current = self.head
        temp = self.head
        while current.next != None:
            temp = current
            current = current.next
        temp.next = None

    def delete_first(self):
        print("Deleting First Element========")
        self.head = self.head.next

    def traversal(self):
        current = self.head
        print("Head is ", self.head.data)
        while current != None:
            print(current.data)
            current = current.next

    def reverse(self):
        temp = None
        current = self.head
        while current != None:
            next = current.next
            current.next = temp
            temp = current
            current = next
        self.head = temp

word = SingleLL()

word.append("egg")
word.append("fish")
word.append("chicken")
word.append("potato")
word.append("tomato")
word.append("brinjal")
# word.traversal()
# word.delete_last()
# word.delete_first()
# word.appendleft("mutton")
# print(word.insert_after("fish","hens"))
# # print("=====================")
# word.reverse()
# word.delete_last()
# word.delete_first()
# word.appendleft("mutton")
# word.appendleft("egg")
# word.appendleft("fish")
word.reverse()
# word.append("sheer-khorma")
word.traversal()
