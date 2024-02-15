# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=ListNode()
        even=ListNode()
        cur_odd=odd
        cur_even=even
        pos=1
        cur=head
        while cur:
            if pos%2 == 0:
                cur_even.next=cur
                cur_even=cur_even.next
            else:
                cur_odd.next=cur
                cur_odd=cur_odd.next
            cur=cur.next
            pos+=1
        cur_odd.next=None
        cur_even.next=None
        answer=ListNode()
        cur=answer
        odd=odd.next
        even=even.next
        while odd or even:
            if odd:
                cur.next=odd
                odd=odd.next
            else:
                cur.next=even
                even=even.next
            cur=cur.next
        cur.next=None
        return answer.next
        



        

        
            
        
