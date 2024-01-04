class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=defaultdict(int)
        mxm=0
        left=0
        for right in range(len(s)):
            if s[right] in chars and chars[s[right]]>=left:
                left=chars[s[right]]+1
            mxm=max(mxm,right-left+1)
            chars[s[right]]=right
        return mxm