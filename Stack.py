class Stack:

    def __init__(self,max_size) -> None:
        self.stack = []
        self.top = None
        self.max_size = max_size

    def push(self,data):
        if self.top == None:
            self.top = 0
            self.stack.append(data)
        elif self.top == self.max_size-1:
            print("Stack Overflow")
        else:
            self.stack.append(data)
            self.top += 1
    
    def pop(self):
        if self.top == 0:
            self.stack = [] 
            self.top = None
        elif self.top == None:
            print("Stack underflow")
        else:
            self.stack.remove(self.stack[self.top])
            self.top -= 1
    
    def peek(self):
        return None if self.top == None else self.stack[self.top]
    
    def traversal(self):
        print(self.stack)

mystack = Stack(max_size=2)
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.pop()
x = mystack.peek()
print(x)
# mystack.traversal()