class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, val)->None:
        if self.head == None:
            self.head = self.tail = Node(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        self.size += 1

    def delete(self, val:int)->None or Exception:
        if self.head.data == val:
            self.head = self.head.next
            self.size-=1
        else:
            curr = self.head
            while(curr is not None and curr.next is not None):
                if curr.next.data == val:
                    break
                curr = curr.next
            if curr is not None and curr.next.data == val:
                curr.next = curr.next.next
                self.size-=1
            else:
                raise Exception("Element not found")

    def getSize(self)->int:
        return self.size

    def search(self,val:int)->bool:
        curr = self.head
        while curr is not None:
            if curr.data == val:
                return True
            curr = curr.next
        return False

    def printList(self):
        curr = self.head
        while curr is not None:
            print(curr.data,end="->")
            curr = curr.next
        print()


if __name__ == "__main__":
    ll = LinkedList()
    for i in range(1,11):
        ll.insert(i)
    ll.printList()
    print(ll.getSize())

    ll.delete(5)
    ll.printList()
    print(ll.getSize())
    ll.delete(10)
    ll.printList()
    print(ll.getSize())
    ll.delete(1)
    print(ll.getSize())
    ll.printList()
    print(ll.search(7))
    print(ll.search(89))