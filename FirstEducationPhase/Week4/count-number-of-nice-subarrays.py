class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        next_odd_index=len(nums)
        next_odd={}
        for i in range(len(nums)-1,-1,-1):
            next_odd[i]=next_odd_index
            if nums[i]%2 != 0:
                next_odd_index=i
        odds=0
        nice=0
        left=0
        for right in range(len(nums)):
            if nums[right]%2 != 0:
                odds+=1
            while odds==k:
                nice+=(next_odd[right]-right)
                if nums[left]%2!=0:
                    odds-=1
                left+=1
        return nice