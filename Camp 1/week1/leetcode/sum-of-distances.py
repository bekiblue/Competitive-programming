class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        previous_prefix={}
        for index in range(len(nums)):
            if nums[index] in previous_prefix:
                prefix[index]=prefix[previous_prefix[nums[index]][0]]+(previous_prefix[nums[index]][1])*(index-previous_prefix[nums[index]][0])
                previous_prefix[nums[index]][0]=index
                previous_prefix[nums[index]][1]+=1
            else:
                previous_prefix[nums[index]]=[index,1]
        suffix=[0]*len(nums)
        previous_suffix={}
        for index in range(len(nums)-1,-1,-1):
            if nums[index] in previous_suffix:
                suffix[index]=suffix[previous_suffix[nums[index]][0]]+(previous_suffix[nums[index]][1])*(previous_suffix[nums[index]][0]-index)
                previous_suffix[nums[index]][0]=index
                previous_suffix[nums[index]][1]+=1
            else:
                previous_suffix[nums[index]]=[index,1]
        arr=[]
        for i in range(len(nums)):
            arr.append(prefix[i]+suffix[i])
        return arr

        
            