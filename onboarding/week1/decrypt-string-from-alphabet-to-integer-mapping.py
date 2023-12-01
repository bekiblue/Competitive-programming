class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping={}
        answer=""
        for d in range(1,10):
            mapping[str(d)]=chr(97+d-1)
        for d in range(10,27):
            mapping[str(d)+"#"]=chr(96+d)
        cur=0
        while cur<len(s):
            if cur+2 < len(s) and s[cur+2]=="#":
                answer+=mapping[s[cur:cur+3]]
                cur+=3
            else:
                answer+=mapping[s[cur]]
                cur+=1
        return answer

        