class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count=1
        mxm=float("-inf")
        for index in range(1,len(num)):
            if num[index]==num[index-1]:
                count+=1
            else:
                count=1
            if count==3 :
                  mxm=max(int(num[index]),mxm) 
        
        if mxm!=float("-inf"):
            return str(mxm)*3
        else:
            return ""