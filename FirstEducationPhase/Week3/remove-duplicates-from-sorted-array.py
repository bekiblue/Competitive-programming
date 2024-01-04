class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer=0
        for reader in range(1,len(nums)):
            if nums[writer] != nums[reader]:
                writer+=1
                nums[writer]=nums[reader]
        return writer+1
    