class MinHeap():
    def __init__(self,capacity) -> None:
        self.heap = []
        self.capacity = capacity
        self.size = 0

    def is_full(self):
        return self.size == self.capacity
    
    def get_parent_index(self,index):
        return (index-1)//2

    def get_child_index(self,index,is_left):
        if is_left:
            return 2*index+1
        return 2*index+2

    def swap(self,source_index,target_index):
        self.heap[source_index],self.heap[target_index] = self.heap[target_index],self.heap[source_index]

    def insert(self, data):
        if self.is_full():
            return
        
        self.heap.append(data)
        self.size+=1
        self.__heapify_up(self.size-1)

    def __heapify_up(self, index):
        parent_index = self.get_parent_index(index)
        if parent_index>=0:
            if self.heap[index] < self.heap[parent_index]:
                self.swap(index, parent_index)
                self.__heapify_up(parent_index)

    def pop(self) -> int:
        if self.size == 0:
            raise Exception("Heap is empty")
        data = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.heap.pop()
        self.size-=1
        self.__heapify_down(0)
        return data

    def __heapify_down(self,index):
        left_index = self.get_child_index(index, True)
        right_index = self.get_child_index(index, False)
        smaller_index = -1
        if left_index<self.size and self.heap[left_index]< self.heap[index]:
            smaller_index = left_index
        if right_index<self.size and self.heap[right_index]< self.heap[smaller_index]:
            smaller_index = right_index
        if smaller_index > -1 and self.heap[smaller_index] < self.heap[index]:
            self.swap(index,smaller_index)
            self.__heapify_down(smaller_index)


if __name__=="__main__":
    mh = MinHeap(10)

    mh.insert(5)
    mh.insert(2)
    mh.insert(17)
    mh.insert(23)
    mh.insert(3)
    mh.insert(7)
    mh.insert(1)
    mh.insert(6)
    
    print(mh.heap)

    while(mh.size>0):
        print(mh.pop())
    print(mh.heap)