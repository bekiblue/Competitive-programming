class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cur_sum=count=0
        prefix_counter={0:1}
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
            cur_sum+=nums[i]
            if cur_sum-k in prefix_counter:
                count+=prefix_counter[cur_sum-k]
            if cur_sum in prefix_counter:
                prefix_counter[cur_sum]+=1
            else:
                prefix_counter[cur_sum]=1
        return count
        
