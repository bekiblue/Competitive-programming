# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        meet=False
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                meet=True
                break
        return True if meet else False