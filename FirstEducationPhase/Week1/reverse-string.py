class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for index in range(len(s)//2):
            s[index],s[-(index+1)]=s[-(index+1)],s[index]
