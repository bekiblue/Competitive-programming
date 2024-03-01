# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length=0
        itr=head
        while itr:
            length+=1
            itr=itr.next
        answer=[]
        initial=length//k
        greater_nodes=length%k
        cur=head
        start=head
        index=0
        while cur:
            if greater_nodes > 0 and index == initial:
                greater_nodes-=1
                index=0
                answer.append(start)
                start=cur.next
                cur.next=None
                cur=start
                continue
            if greater_nodes==0 and index==initial-1:
                index=0
                answer.append(start)
                start=cur.next
                cur.next=None
                cur=start
                continue
            index+=1
            cur=cur.next
        if len(answer) < k:
            for _ in range(k-len(answer)):
                answer.append(None)
        return answer
            
