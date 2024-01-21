class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        freq=defaultdict(int)
        for right in range(len(s)):
            freq[s[right]]+=1
            if freq["L"]==freq["R"]:
                freq=defaultdict(int)
                count+=1
        return count if not freq else 0