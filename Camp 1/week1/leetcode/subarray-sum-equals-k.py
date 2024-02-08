class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums=defaultdict(int)
        prefix_sums[0]=1
        count=0
        running_sum=0
        for num in nums:
            running_sum+=num
            if running_sum-k in prefix_sums:
                count+=prefix_sums[running_sum-k]
            prefix_sums[running_sum]+=1
        return count