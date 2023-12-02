class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                
        length =0 
        winStart=windEnd=0
        visited = {}

        for winEnd in range(len(s)): 
            if s[winEnd] in visited:
                winStart = max(winStart, visited[s[winEnd]] + 1)
                
            length = max(length, winEnd - winStart + 1)
            visited[s[winEnd]] = winEnd
        
        return length 
