# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        back,cur=None,head
        while cur:
            front=cur.next
            cur.next=back
            back=cur
            cur=front
        return back