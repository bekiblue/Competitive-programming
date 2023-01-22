# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        itr=head
        count=0
        while itr:
            itr=itr.next
            count+=1
        
        if count==0 :
            pass
        elif count==1:
            dummy.next=None
        elif n==count:
            dummy.next=head.next
        elif n==1:
            itr=dummy
            while itr.next.next:
                itr=itr.next  
            itr.next=None
        else:
            index=0
            cur=head
            while cur:
                if index==count-n-1:
                    cur.next=cur.next.next
                index+=1
                cur=cur.next
    
        return dummy.next
