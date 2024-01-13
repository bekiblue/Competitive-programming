class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s=defaultdict(int)
        freq_t=defaultdict(int)
        for index in range(len(s)):
            freq_s[s[index]]+=1
            freq_t[t[index]]+=1
        steps=0
        for char in freq_s:
            if freq_t[char] < freq_s[char]:
                steps+=(freq_s[char]-freq_t[char])
        return steps 
