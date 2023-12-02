class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,cur=None,head
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp 
        head=prev

        return head
