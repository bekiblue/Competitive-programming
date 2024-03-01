class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinict=len(Counter(nums))
        window=defaultdict(int)
        left=0
        complete=0
        for right in range(len(nums)):
            window[nums[right]]+=1
            while left<= right and len(window)==distinict:
                complete+=(len(nums)-right)
                window[nums[left]]-=1
                if window[nums[left]]==0:
                    del window[nums[left]]
                left+=1
        return complete



