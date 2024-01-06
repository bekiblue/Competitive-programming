class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        nums.sort()
        for index in range(len(nums)-2):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            left=index+1
            right=len(nums)-1
            while left < right :
                if nums[left]+nums[right] < -nums[index]:
                    left+=1
                elif nums[left]+nums[right] > -nums[index]:
                    right-=1
                else:
                    answer.append([nums[index],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    left+=1
        return answer
        