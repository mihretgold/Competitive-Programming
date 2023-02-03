class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
        
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i = 0
        found = -1
        if self.head == None:
            return -1
        else:
            temp = self.head
            while i < index and temp.next != None:
                temp = temp.next
                i += 1
            if i == index:
                found = temp.val
            

        return found     

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        temp = self.head
        newNode.next = temp
        self.head = newNode
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        curr = self.head
        temp = None
        if index == 0:
            self.addAtHead(val)
        else:
            i = 0
            while i < index-1 and curr.next != None:
                curr = curr.next
                i += 1
                
            if curr:
                temp = curr.next
                curr.next = newNode
                newNode.next = temp
        
            

    def deleteAtIndex(self, index: int) -> None:
        newN = self.head
        i = 0
        while i < index-1 and newN.next != None:
            newN = newN.next
            i += 1
        node = self.head
        while(node):
            print(node.val)
            node = node.next
        print("after")
        if index == 0:
            self.head = self.head.next
        elif newN and newN.next:
            newN.next = newN.next.next
        node = self.head
        while(node):
            print(node.val)
            node = node.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)