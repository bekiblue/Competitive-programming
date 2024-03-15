class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find the index of the last number less than the target
        start = -1
        left = 0
        right = len(nums) - 1

        while left <= right :
            mid = (left + right) // 2
            if nums[mid] == target :
                right = mid
                start = right  
                if left == right :
                    break               
            elif nums[mid] < target:
                left = mid + 1 
            else:
                right = mid - 1
        # Find the index of the first number greater than the target
        left = 0
        right = len(nums) - 1
        end = -1
        while left <= right :
            mid = (left + right) // 2
            if nums[mid] == target :
                left = mid
                end = left
                if left == right or right == left + 1 :
                    if  nums[left] == nums[right] :
                        end = right
                    break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1 
                
        return [start , end]