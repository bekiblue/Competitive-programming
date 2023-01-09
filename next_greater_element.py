class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums1)):
            ans.append(-1)
            for j in range(len(nums2)):
                if nums2[j]==nums1[i]:
                    for z in nums2[j+1:]:
                        if z>nums1[i]:
                            ans[i]=z
                            break
                    break
        return ans
                

        

        
