class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders=defaultdict(int)
        running_sum=0
        count=0
        for num in nums:
            running_sum+=num
            if running_sum%k == 0 :
                count+=1
            if running_sum%k in remainders:
                count+=remainders[running_sum%k]
            remainders[running_sum%k]+=1
        return count
