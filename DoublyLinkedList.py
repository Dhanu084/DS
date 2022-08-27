class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = self.tail = None

    def insert(self, val:int):
        if self.head is None:
            self.head = self.tail = Node(val)
        else:
            curr_tail = self.tail
            self.tail.next = Node(val)
            self.tail = self.tail.next
            self.tail.prev = curr_tail
            curr_tail.next = self.tail


    def delete(self, val:int)->None:
        if self.isExists(val)==False:
            return
        if self.head.data == val:
            if self.head==self.tail:
                self.head = self.tail = None
            else:
                curr_next = self.head.next
                self.head.next = self.head.prev = None
                self.head = curr_next

        else:
            curr = self.head
            while curr is not None and curr.data != val:
                curr = curr.next
            if curr == self.tail:
                prev = curr.prev
                self.tail.prev = None
                prev.next = None
                self.tail = prev
            else:
                prev = curr.prev
                next = curr.next
                prev.next = next
                next.prev = prev
                curr.prev=curr.next = None
    
    def printList(self)->None:
        curr = self.head
        while curr is not None:
            print(curr.data,end='->')
            curr = curr.next
        print()

    def isExists(self, val)->bool:
        curr = self.head
        while curr is not None:
            if curr.data == val:
                return True
            curr = curr.next
        return False


if __name__=="__main__":
    dll = DoublyLinkedList()

    for i in range(1,6):
        dll.insert(i)

    dll.printList()

    dll.insert(1)
    dll.insert(5)
    dll.insert(1)
    dll.insert(1)

    dll.printList()

    dll.delete(1)
    dll.printList()

    dll.delete(1)
    dll.printList()

    dll.delete(1)
    dll.printList()

    dll.delete(1)
    dll.printList()

    dll.insert(1)
    dll.printList()


