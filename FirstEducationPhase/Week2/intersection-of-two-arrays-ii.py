from collections import Counter 
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq=Counter(nums2)
        answer=[]
        for num in nums1:
            if num in freq:
                freq[num]-=1
                if freq[num]==0:
                    del freq[num]
                answer.append(num)
        return answer
        