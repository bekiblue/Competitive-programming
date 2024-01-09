class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #i don't need to flip in the implemntation
        # i just need to find the longest subarray that contain at most k zeros
        window_left=0
        count=0
        longest=0
        for window_right in range(len(nums)):
            if nums[window_right]==0:
                count+=1
            while count>k:
                if nums[window_left]==0:
                    count-=1
                window_left+=1
            longest=max(longest,window_right-window_left+1)
        return longest

