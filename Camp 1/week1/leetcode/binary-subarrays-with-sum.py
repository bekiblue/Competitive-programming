class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixes=defaultdict(int)
        prefixes[0]=1
        count=0
        running_sum=0
        for num in nums:
            running_sum+=num
            if running_sum-goal in prefixes:
                count+=prefixes[running_sum-goal]
            prefixes[running_sum]+=1
        return count
