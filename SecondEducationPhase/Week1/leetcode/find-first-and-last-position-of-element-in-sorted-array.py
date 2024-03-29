class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find the start index of number if exists
        left = 0
        right = len(nums) - 1

        while left <= right :
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1 
            else:
                right = mid - 1
        start = left if (left < len(nums) and nums[left] == target) else -1
        # Find the end index of the number if exists
        left = 0
        right = len(nums) - 1

        while left <= right :
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1 
        end = right if (right >= 0 and nums[right] == target) else -1
        
        return [start , end]