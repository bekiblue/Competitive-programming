class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #It's finding the longest substring such that the letters to be replaced(the difference between the length of the substring and the frequency of the most occuring elemnt in the substring) is less than or equal to k
        longest=0
        mxm=0
        freq=defaultdict(int)
        left=0
        for right in range(len(s)):
            freq[s[right]]+=1
            if freq[s[right]] > mxm:
                mxm=freq[s[right]]
            while (right-left+1) - mxm > k:
                freq[s[left]]-=1
                mxm=max(freq.values())
                left+=1
            longest=max(longest,right-left+1)
        return longest
