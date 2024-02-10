class Solution:
    def maxScore(self, s: str) -> int:
        prefix=[]
        running_sum=0
        for digit in s:
            prefix.append(running_sum)
            if digit=="0":
                running_sum+=1
        suffix=[0]*(len(s))
        running_sum=0
        for index in range(len(s)-1,-1,-1):
            suffix[index]=running_sum
            if s[index]=="1":
                running_sum+=1
        mxm_score=float("-inf")
        for index in range(1,len(s)):
            if prefix[index]+suffix[index-1] > mxm_score:
                mxm_score=prefix[index]+suffix[index-1]
        return mxm_score





            

