class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        positions=[0]*(len(nums))
        for request in requests:
            positions[request[0]]+=1
            if request[1] < len(nums)-1:
                positions[request[1]+1]-=1
        prefix=[]
        running_sum=0
        for position in positions:
            running_sum+=position
            prefix.append(running_sum)
        prefix.sort()
        nums.sort()
        answer=0
        for index in range(len(nums)):
            answer+=prefix[index]*nums[index]
        return answer%(10**9+7)

        


