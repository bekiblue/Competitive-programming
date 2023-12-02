class Solution:
    def numIdenticalPairs(self, nums ):
        self.good_num = 0 
        for i in range(len(nums)-1):
            for j in nums[i+1:]:
                if nums[i]==j:
                    self.good_num+=1
        return self.good_num
