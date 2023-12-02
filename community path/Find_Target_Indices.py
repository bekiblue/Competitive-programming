class Solution:
    def targetIndices(self, nums, target):
        
        for i in range(len(nums)):
            temp = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[temp]:
                    temp = j
            nums[i], nums[temp] = nums[temp], nums[i]
        output = []   
        for i in range(len(nums)):
            if nums[i] == target:
                output.append(i)
        return output
                
        
