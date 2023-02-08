class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        length = 1
        winStart = 0
        winEnd = 0
        seen = {}
        
        
        while winEnd < len(s):
            
            if s[winEnd] in seen:
                winStart = max(winStart, seen[s[winEnd]] + 1)
                
            length = max(length, winEnd - winStart + 1)
 
            seen[s[winEnd]] = winEnd
            winEnd += 1
        
        return length
