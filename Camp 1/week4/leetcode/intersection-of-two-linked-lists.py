# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA=0
        itr=headA
        while itr:
            lenA+=1
            itr=itr.next
        lenB=0
        cur=headB
        while cur:
            lenB+=1
            cur=cur.next
        if lenA >= lenB:
            itr=headA
            for _ in range(lenA-lenB):
                itr=itr.next
            pointerA=itr
            pointerB=headB
        else:
            itr=headB
            for _ in range(lenB-lenA):
                itr=itr.next
            pointerA=headA
            pointerB=itr
        while pointerA:
            if pointerA==pointerB:
                return pointerA
            pointerA=pointerA.next
            pointerB=pointerB.next
        return None
        

