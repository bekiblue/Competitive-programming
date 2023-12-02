class Solution:
    def isValid(self, s: str) -> bool:
        pair= { ')':'(', ']': '[', '}':'{' }
        opening=set(['[','{','('])
        stack = []
        if len(s)%2 != 0:
            return False
        for char in s:
            if char in opening:
                stack.append(char)
            elif stack and pair[char]==stack[-1]  :
                stack.pop(-1)
            else :
                return False
        
        if stack:
           return  False
        else:
            return True
