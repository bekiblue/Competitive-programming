class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets=[[]]

        def backtrack(path,index):

            if index >= len(nums):
                return 
        
            path.append(nums[index])
            subsets.append(path[:])
            backtrack(path,index+1)
            last = path.pop()

            while index + 1 < len(nums) and last == nums[index+1]:
                index +=1
            #don't pick
            backtrack(path,index+1)
            
        backtrack([],0)

        return subsets