class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled=[""]*len(s)
        for index in range(len(s)):
            shuffled[indices[index]]=s[index]
        return "".join(shuffled)
