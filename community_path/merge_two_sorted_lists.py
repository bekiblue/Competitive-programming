# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
                return list1
        if list1==None:
            cur=list2
            val1=list1
            val2=cur.next
        elif list2==None:
            cur=list1
            val1=cur.next
            val2=list2
        
        elif list1.val <= list2.val :
            cur=list1
            val1=cur.next
            val2=list2
        elif list1.val > list2.val:
            cur=list2
            val1=list1
            val2=cur.next

        
        answer=cur
        # cur=min(list1,list2,key=lambda x:x.val)

        while val1!=None and val2!=None:
            if val1.val <= val2.val:
                cur.next=val1
                cur=val1
                val1=cur.next
            else:
                cur.next=val2
                cur=val2
                val2=cur.next
            # cur.next=min(val1,val2,key=lambda x : x.val )
            # cur=cur.next
            # min(val1,val2,key=lambda x : x.val )=cur.next
        if val1==None:
            cur.next=val2
        elif val2==None:
            cur.next=val1
        else:
            return answer
        return answer
   

        

        
    
