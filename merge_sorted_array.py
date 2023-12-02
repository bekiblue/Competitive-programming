class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        j=0
        k=0
        copy=nums1[0:m]
        while  i<m and j<n: 
            if copy[i] <= nums2[j]:
                nums1[k]=copy[i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            k+=1
        while i<m:
            nums1[k]=copy[i]
            i+=1
            k+=1
        
        while j<n:
            nums1[k]=nums2[j]
            j+=1
            k+=1
