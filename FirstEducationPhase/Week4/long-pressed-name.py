class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0]:
            return False
        p1=0
        p2=0
        while p1 < len(name) and p2<len(typed):
            if name[p1] != typed[p2]:
                if name[p1-1] == typed[p2]:
                    p2+=1
                else:
                    return False
            else:
                p1+=1
                p2+=1 
        while p1==len(name) and p2 < len(typed) and typed[p2]==name[-1]:
            p2+=1
        return True if p1==len(name) and p2==len(typed) else False