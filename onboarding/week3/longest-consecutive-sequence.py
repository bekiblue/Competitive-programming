class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers=set(nums)
        mxm=0
        for num in nums:
            if num-1 not in numbers:
                count=1
                while num+1 in numbers:
                    num+=1
                    count+=1
                mxm=max(mxm,count)
        return mxm