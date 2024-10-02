class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        answer = []
        index = 0
        while index < len(nums) -1:
            if nums[index] != 0 and nums[index] == nums[index+1]:
                answer.append( 2*nums[index] )
                nums[index+1] = 0
                index += 2
                continue
            if nums[index] != 0:
                answer.append (nums[index])
            index += 1
            
        answer.append(nums[-1])
        answer.extend([0]*(len(nums)-len(answer)))
        return answer
        
