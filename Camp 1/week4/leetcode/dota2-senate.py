class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_count=senate.count("R")
        d_count=len(senate) - r_count
        _senate=deque(senate)
        r_ban=0
        d_ban=0
        while r_count and d_count:
            if _senate[0]=="R" and r_ban :
                _senate.popleft()
                r_ban-=1
                continue
            if _senate[0]=="D" and d_ban:
                _senate.popleft()
                d_ban-=1
                continue
            cur=_senate.popleft()
            if cur=="R":
                d_ban+=1
                d_count-=1               
            else:
                r_ban+=1
                r_count-=1
            _senate.append(cur)
        return "Radiant" if r_count else "Dire"

            
            