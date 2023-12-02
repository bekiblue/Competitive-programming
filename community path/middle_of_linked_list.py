class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = second = head
        while first and first.next:
            second = second.next
            first = first.next.next
        return second
