# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        itr=head
        arr=[]
        stack=[]
        next_dict={}
        while itr:
            while stack and stack[-1].val<itr.val:
                next_dict[stack.pop()]=itr.val
            stack.append(itr)
            itr=itr.next
        for i in stack:
            next_dict[i]=0
        itr=head
        while itr:
            arr.append(next_dict[itr])
            itr=itr.next
        return arr
        
