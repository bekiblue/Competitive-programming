class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer=[0]*2*n
        for index in range(2*n):
            if index%2==0:
                answer[index]=nums[index//2]
            else:
                answer[index]=nums[n+(index-1)//2]
        return answer
