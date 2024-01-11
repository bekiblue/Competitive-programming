class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #holder and seeker
        k=0
        holder=0    
        for seeker in range(len(nums)):
            if nums[seeker]!=val:
                nums[holder]=nums[seeker]
                holder+=1
                k+=1
        return k