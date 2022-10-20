class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                reverse = s[stack[-1]: i+1]
                s = s[:stack[-1]] + reverse[::-1] + s[i+1:]
                del stack[-1]
        
        ans = ''
        bracket=set(['(',')'])
        for i in s:
            if i not in bracket:
                ans += i
        return ans
                
                
            
