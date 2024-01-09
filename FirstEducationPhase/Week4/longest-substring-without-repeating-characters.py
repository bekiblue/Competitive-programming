class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_left=0
        window_right=0
        last_seen={}
        longest=0
        for window_right in range(len(s)):
            if s[window_right] in last_seen and window_left <= last_seen[s[window_right]]:
                window_left=last_seen[s[window_right]]+1
            else:
                longest=max(longest,window_right-window_left+1)
            last_seen[s[window_right]]=window_right
        return longest