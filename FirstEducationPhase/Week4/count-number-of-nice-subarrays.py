class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # for each index count the nice subarrays that end at that index
        total=0
        odds=0
        nice=0
        left=0
        for right in range(len(nums)):
            if nums[right]%2 != 0:
                odds+=1
                # if an odd number odd is encountered my nice subarray will become bad 
                nice=0 
            while odds==k:
                #count the number all nice subarrays that end at this index
                nice+=1
                if nums[left]%2!= 0:
                    odds-=1
                left+=1
            #add the number of nice subarrays at this index to the total
            total+=nice
        return total


