class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed=[]
        for index in range(0,len(nums),2):
            decompressed+=[nums[index+1]]*nums[index]
        return decompressed