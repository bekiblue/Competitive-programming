class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index={}
        for i in range(len(arr2)):
            index[arr2[i]]=i
        return sorted(arr1,key=lambda num: index[num] if num in index else num+len(arr2))
        
        
