class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for index in range(len(palindrome)//2):
            if palindrome[index] != "a":
                return palindrome[:index]+"a"+palindrome[index+1:]
        return palindrome[:len(palindrome)-1]+"b" if len(palindrome)>1 else ""
        

