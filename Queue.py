class Queue():
    def __init__(self,size) -> None:
        self.size = size
        self.queue = [0]*size
        self.index = 0

    def enqueue(self, val):
        if self.index >= self.size:
            return
        self.queue[self.index] = val
        self.index+=1

    
    def dequeue(self):
        if self.index<0:
            return
        try:
            self.queue.pop(0)
            self.index-=1
        except Exception:
            print()


    def get_front(self):
        return self.queue[0] if self.index()>0 else None

    def printQueue(self):
        for item in self.queue:
            print(item,end='-')
        print()


if __name__=="__main__":
    q = Queue(2)
    
    for i in range(0,3):
        q.enqueue(i)
 
    q.dequeue()
    q.printQueue()
    q.dequeue()
    q.printQueue()
    q.dequeue()
    q.printQueue()
    

    