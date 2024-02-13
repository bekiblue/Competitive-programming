class Node:
    def __init__(self,value,next=None):
        self.val=value
        self.next=next
class MyLinkedList:

    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        if not self.head:
            return -1   
        count=0
        cur=self.head
        while cur:
            if count==index:
                break
            cur=cur.next
            count+=1
        else:
            return -1
        return cur.val
    def addAtHead(self, val: int) -> None:
        self.head=Node(val,self.head)
    def addAtTail(self, val: int) -> None:
        new=Node(val)
        if not self.head:
            self.head=new
            return
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=new
    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return
        cur=self.head
        count=0
        while cur:
            if count==index-1:
                cur.next=Node(val,cur.next)
                break
            cur=cur.next
            count+=1
    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index==0:
            self.head=self.head.next
        cur=self.head
        count=0
        while cur:
            if count==index-1:
                if cur.next:
                    cur.next=cur.next.next
                break
            cur=cur.next
            count+=1
        




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)