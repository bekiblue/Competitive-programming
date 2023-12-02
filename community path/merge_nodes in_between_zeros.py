# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        itr=cur
        while itr:
            if itr.val==0 and itr.next!=None:
                cur=itr
                itr=itr.next
            elif itr.val==0 and itr.next==None:
                cur.next=None
                itr=itr.next
            else:
                cur.next=itr.next
                cur.val+=itr.val
                itr=cur.next
        return head
        
            
