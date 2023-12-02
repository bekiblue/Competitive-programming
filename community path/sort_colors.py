class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero=0
        one=0
        n=len(nums)
        for i in nums:
            if i == 0 :
                zero+=1
            if i == 1:
                one+=1
        two=n-(zero+one)
        nums.clear()
        for i in range(zero):
            nums.append(0)
        for i in range(one):
            nums.append(1)
        for i in range(two):
            nums.append(2)
