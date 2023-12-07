class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        answer=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
            if freq[num] == len(nums)//3+1:
                answer.append(num)
        return answer