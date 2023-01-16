from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=sorted(Counter(nums).items(),key= lambda x : -x[1])
        answer=[]
        for i in range(k):
            answer.append(freq[i][0])
        return answer
