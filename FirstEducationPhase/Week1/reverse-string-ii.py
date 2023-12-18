class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left=0
        for segment in range(len(s)//(2*k)):
            s = s[:left]+s[left:left+k][::-1]+s[left+k:]
            left+=2*k
        
        return s[:left]+s[left:][::-1] if len(s) % (2*k) < k else s[:left]+s[left:left+k][::-1]+s[left+k:]