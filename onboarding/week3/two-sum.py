class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        for index in range(len(nums)):
            if target-nums[index] in visited:
                return [visited[target-nums[index]],index]
            visited[nums[index]]=index
