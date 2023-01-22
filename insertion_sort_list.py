# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        dummy=ListNode()
        itr=head
        while itr :
            cur=dummy
            while cur.next and itr.val >= cur.next.val:
                cur=cur.next
           
            cur.next=ListNode(itr.val,cur.next)
                    
                    
            itr=itr.next

        return dummy.next
            
