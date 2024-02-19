class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        nums=defaultdict(int)
        total=0
        for answer in answers:
            if answer not in nums :
                total+=(answer+1)

            nums[answer]+=1
            if nums[answer] > answer+1 :
                total+=(answer+1)
                nums[answer]-= (answer+1)
            
        return total 
