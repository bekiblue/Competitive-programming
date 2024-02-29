# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        
        prev_start=prev
        current = prev.next
        end=current
        prev=None
        for _ in range(right - left+1):
            next_node = current.next
            current.next=prev
            prev=current
            current=next_node
        prev_start.next=prev
        end.next=current

        return dummy.next