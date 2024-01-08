class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff=float('inf')
        for index in range(len(nums)-2):
            left=index+1
            right=len(nums)-1
            while left < right:
                if nums[left]+nums[right]+nums[index] < target:
                    if target-(nums[left]+nums[right]+nums[index]) < diff:
                        closest=nums[left]+nums[right]+nums[index]
                        diff=target-closest
                    left+=1
                elif nums[left]+nums[right]+nums[index] > target:
                    if (nums[left]+nums[right]+nums[index])-target < diff:
                        closest=nums[left]+nums[right]+nums[index]
                        diff=closest-target
                    right-=1
                else:
                    return nums[left]+nums[right]+nums[index]
        return closest
                    