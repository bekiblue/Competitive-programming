class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        p_p={}
        for idx in range(len(nums)):
            if nums[idx] in p_p:
                prefix[idx]=prefix[p_p[nums[idx]][0]]+(p_p[nums[idx]][1])*(idx-p_p[nums[idx]][0])
                p_p[nums[idx]][0]=idx
                p_p[nums[idx]][1]+=1
            else:
                p_p[nums[idx]]=[idx,1]
        print(prefix)
        suffix=[0]*len(nums)
        p_s={}
        for idx in range(len(nums)-1,-1,-1):
            if nums[idx] in p_s:
                suffix[idx]=suffix[p_s[nums[idx]][0]]+(p_s[nums[idx]][1])*(p_s[nums[idx]][0]-idx)
                p_s[nums[idx]][0]=idx
                p_s[nums[idx]][1]+=1
            else:
                p_s[nums[idx]]=[idx,1]
        arr=[]
        for i in range(len(nums)):
            arr.append(prefix[i]+suffix[i])
        return arr

        
            
