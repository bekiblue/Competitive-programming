# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        while list1 or list2:
            if not list1 or list2 and list2.val < list1.val:
                cur.next=list2
                list2=list2.next
            else:
                cur.next=list1
                list1=list1.next
            cur=cur.next
        return dummy.next





