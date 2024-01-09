class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # i don't need to delete the element
        # i can just find the longest subarray that contains at most one zero
        # return the longest subarray length minus one(deleted)
        window_left=0
        window_right=0
        longest=0
        count=0
        zero_position=0
        for window_right in range(len(nums)):
            if nums[window_right]==0:
                if count==0:
                    count+=1
                    zero_position=window_right
                    longest=max(longest,window_right-window_left+1)
                else:
                    window_left=zero_position+1
                    zero_position=window_right
            else:
                longest=max(longest,window_right-window_left+1)
        return longest-1