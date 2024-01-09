class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={"a","e","i","o","u"}
        count=0
        for index in range(k):
            if s[index] in vowels:
                count+=1
        mxm=count
        for char in range(k,len(s)):
            if s[char] in vowels:
                count+=1
            if s[char-k] in vowels:
                count-=1
            mxm=max(mxm,count)
        return mxm