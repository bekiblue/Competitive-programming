class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for x,y,z in zip(s,s[1:],s[2:]):
            if x!=y and y!=z and x!=z:
                count+=1
        return count
            
                


