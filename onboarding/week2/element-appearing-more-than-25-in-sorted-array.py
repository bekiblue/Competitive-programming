class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq={}
        n=0.25*len(arr)
        for num in arr:
            freq[num]=freq.get(num,0)+1
            if freq[num] > n:
                return num
        