class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        greater=[]
        count=0
        for num in nums:
            if num < pivot :
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                count+=1
        return less+[pivot]*count+greater