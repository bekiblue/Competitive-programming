# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(float("-inf"),head)
        prev=dummy
        itr=head
        while itr:
            if prev.val <= itr.val:
                prev=itr
                itr=itr.next
                continue
            cur=dummy
            while cur.next and itr.val >= cur.next.val:
                cur=cur.next
            prev.next=itr.next
            prev=itr
            itr.next=cur.next
            cur.next=itr
            itr=itr.next
        return dummy.next  