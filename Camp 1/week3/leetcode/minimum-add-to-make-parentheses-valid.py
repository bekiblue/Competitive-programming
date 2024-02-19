class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening=[]
        result=0
        for brace in s:
            if brace==")" and opening:
                opening.pop()
            elif brace==")" and not opening:
                result+=1
            else:
                opening.append(brace)
        return len(opening)+result
