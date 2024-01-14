class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes={}
        left=0
        for index,num in enumerate(nums):
            while index - left  > k:
                left+=1 
            if num in indexes and indexes[num] >= left:
                    return True
            indexes[num]=index
        return False

            
            
