# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        gap=1
        while cur.next:
            if gap==n+1:
                break
            cur=cur.next
            gap+=1
        else:
            if gap==n:
                return head.next
        slow=head
        fast=cur
        while fast.next:
            slow=slow.next
            fast=fast.next  
        slow.next=slow.next.next
        return head
        
        
            
        
            
            