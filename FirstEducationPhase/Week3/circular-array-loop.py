class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        checked=set()
        for index in range(len(nums)):
            if index in checked :
                continue
            direction= 1 if nums[index] > 0 else -1
            next_direction= 1 if nums[index] > 0 else -1
            cycle=set()
            next_index=(index+nums[index])%len(nums) 
            while next_index not in cycle and direction == next_direction and   next_index != index:
                cycle.add(index)
                checked.add(index)
                index=next_index
                next_index=(index+nums[index])%len(nums) 
                next_direction= 1 if nums[index] > 0 else -1
            if direction==next_direction and next_index != index:
               return True
        return False
            
            