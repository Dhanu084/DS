class Stack():
    def __init__(self,size = 3) -> None:
        self.size = size
        self.stack = [0]*size
        self.index = 0

    def push(self,val:int)->None:
        if self.index >= self.size:
            return
        self.stack[self.index] = val
        self.index+=1
    
    def pop(self)->int:
        if self.index <= 0:
            return -1
        self.index-=1
        return self.stack.pop()

    def printStack(self):
        for item in self.stack:
            print(item,end="-")
        print()
    
    def top(self):
        if self.index<=0:
            return -1
        return self.stack[self.index-1]

if __name__=="__main__":
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)

    print(st.top())

    for i in range(0,3):
        print(st.pop())
    print(st.pop())

    print(st.top())