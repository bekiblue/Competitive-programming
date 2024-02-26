class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mon_incr=[]
        smallest_smaller=[]
        for index,num in enumerate(nums):
            while mon_incr and num < nums[mon_incr[-1]]:
                mon_incr.pop()
            if mon_incr:
                smallest_smaller.append(nums[mon_incr[0]])
            else:
                smallest_smaller.append(float("inf"))
            mon_incr.append(index) 
        mon_decr=[]
        for index in range(len(nums)-1,-1,-1):
            i=None
            while mon_decr and nums[index] > nums[mon_decr[-1]]:
                i=mon_decr.pop()
            if i is not None and smallest_smaller[index] < nums[i]:
                return True
            mon_decr.append(index)
        return False