class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq=Counter(s)
        if len(freq)==1:
            return freq[s[0]]
        length=0
        odd=True
        for char in freq:
            if freq[char]%2 and odd:
                length+=1
                odd=False
            length+=2*(freq[char]//2)
        return length
        