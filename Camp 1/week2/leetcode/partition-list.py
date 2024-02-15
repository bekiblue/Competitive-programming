# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less=ListNode()
        greater=ListNode()
        cur_less=less
        cur_greater=greater
        cur=head
        while cur:
            if cur.val < x:
                cur_less.next=cur
                cur_less=cur_less.next
            else:
                cur_greater.next=cur
                cur_greater=cur_greater.next
            cur=cur.next
        cur_less.next=greater.next
        cur_greater.next=None
        return less.next
        