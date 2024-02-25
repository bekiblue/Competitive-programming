class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mon_decr=[] #It stores index of elements whose next greater element have not been determined in decreasing order 
        next_greater=[-1]*len(nums)
        for index in range(2*len(nums)):
            num=nums[index%len(nums)]
            while mon_decr and num > nums[mon_decr[-1]]:
                popped_index=mon_decr.pop()
                next_greater[popped_index]=num
            mon_decr.append(index%len(nums))
        return next_greater
        
        

