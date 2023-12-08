class Solution:
    def largestOddNumber(self, num: str) -> str:
        for index in range(len(num)-1,-1,-1):
            if int(num[index])%2 != 0:
                return num[:index+1]
        return ""