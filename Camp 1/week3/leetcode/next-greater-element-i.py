class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        next_greatest={}
        for num in nums2:
            while stack and stack[-1]<num:
                next_greatest[stack.pop()]=num
            stack.append(num)
        for num in stack:
            next_greatest[num]=-1
        for idx in range(len(nums1)):
            nums1[idx]=next_greatest[nums1[idx]]
        
        return nums1
                

        

        