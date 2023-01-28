class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum={0:1}
        cur_sum=0
        count=0

        for i in nums:
            cur_sum+=i
            if cur_sum-k in prefix_sum :
                count+= prefix_sum[cur_sum-k]
            if cur_sum in prefix_sum:
                prefix_sum[cur_sum]+=1
            else:
                prefix_sum[cur_sum]=1
            
            
        return count
