class Solution:
    def removeStars(self, s: str) -> str:
        chars=[]
        for char in s:
            if char == "*":
                chars.pop()
            else:
                chars.append(char)
        return "".join(chars)