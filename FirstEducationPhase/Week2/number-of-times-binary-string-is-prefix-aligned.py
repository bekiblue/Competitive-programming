class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        mxm=0
        count=0
        for step in range(1,len(flips)+1):
            mxm=max(mxm,flips[step-1])
            if step==mxm:
                count+=1
        return count
