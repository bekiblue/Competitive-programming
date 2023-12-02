# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        l = r = head
        while r:
            while r and l.val == r.val:
                r = r.next
            if l.next == r:
                cur.next = l
                cur = cur.next
            l = r
        cur.next = None
        
        return dummy.next
