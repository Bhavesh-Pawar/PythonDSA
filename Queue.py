class Queue:
    
    def __init__(self,max_size) -> None:
        
        self.queue = []
        self.front = None
        self.rear = None
        self.max_size = max_size

    def enqueue(self,data):
        if self.front == None and self.rear == None:
            self.front , self.rear = 0 , 0
            self.queue.append(data)
        elif self.rear == self.max_size - 1:
            print("Queue is full")
        else:
            self.queue.append(data) 
            self.rear += 1

    def dequeue(self,data):
        if self.front == None and self.rear == None:
            self.front , self.rear = 0 , 0
            self.queue.append(data)
        elif self.rear == self.max_size - 1:
            print("Queue is full")
        else:
            self.queue.append(data) 
            self.rear += 1

q = Queue(max_size=2)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
