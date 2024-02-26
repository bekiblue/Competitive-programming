class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mono_decr=[]
        smallest=[]
        cur_smallest=0
        for index,num in enumerate(nums):
            # Handles for keeping the smallest element index upto current index
            if num < nums[cur_smallest]:
                cur_smallest=index
            smallest.append(cur_smallest)

            #updates the stack  
            while mono_decr and num >= nums[mono_decr[-1]]:
                mono_decr.pop()

            #return True if there is a previous greater element and the smallest element upto that greater element index is less than the current element 
            if mono_decr and nums[smallest[mono_decr[-1]]] < num:
                    return True
            mono_decr.append(index) 

        return False