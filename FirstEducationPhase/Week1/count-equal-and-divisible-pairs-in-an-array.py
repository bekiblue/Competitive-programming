class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        divisible=defaultdict(int)
        notDivisible=defaultdict(list)
        count=0
        for index,num in enumerate(nums):
            if index%k==0 :
                count+= len(notDivisible[num])+ divisible[num]
                divisible[num]+=1 
            else:
                count+= divisible[num]
                for idx in notDivisible[num]:
                    if (idx*index)%k==0:
                        count+=1
                notDivisible[num].append(index)
        return count