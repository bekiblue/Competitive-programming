class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char: index for index, char in enumerate(s)}
        end = anchor = 0
        ans = []
        for index, char in enumerate(s):
            end = max(end, last[char])
            if index == end:
                ans.append(end-anchor+1)
                anchor = end + 1
        return ans 
