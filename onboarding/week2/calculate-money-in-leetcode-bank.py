class Solution:
    def totalMoney(self, n: int) -> int:
        return 28*((n-1)//7)+7*(((n-1)//7)*(((n-1)//7)-1))//2+sum(range((n-1)//7+1,(n-1)//7+((n-1)%7)+2))