# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        size = len(lists)
        interval = 1
        while interval < size:
            for i in range(0, size - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if size > 0 else None

    def merge2Lists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l1
                l1 = cur.next.next
            cur = cur.next

        if not l1:
            cur.next=l2
        else:
            cur.next=l1

        return dummy.next
