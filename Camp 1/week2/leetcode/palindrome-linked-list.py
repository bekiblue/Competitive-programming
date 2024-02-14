# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if fast==slow:
            return True
        if fast:
            slow=slow.next
        prev,cur=None,slow
        while cur:
            front=cur.next
            cur.next=prev
            prev=cur
            cur=front
        forward,backward=head,prev
        while backward:
            if forward.val != backward.val:
                return False
            forward,backward=forward.next,backward.next
        return True
        
        