class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        opening=["("] #Initialize the opening braces stack with "(" as the string is balanced 
        score=0
        for index in range(1,len(s)):
            if s[index] == ")":
                opening.pop()
                if s[index-1] == "(":
                    score+=(2**len(opening))
            else:
                opening.append(s[index])
        return score