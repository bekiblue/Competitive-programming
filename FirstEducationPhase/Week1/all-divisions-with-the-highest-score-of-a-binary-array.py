class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left=0
        right=sum(nums)
        mxm=left+right
        answer=[0]
        for index in range(1,len(nums)+1):
            if nums[index-1]==1:
                right-=1
            else:
                left+=1
            if left + right > mxm:
                mxm=left+right
                answer=[index]
            elif left + right == mxm:
                answer.append(index)              
        return answer
        

            
