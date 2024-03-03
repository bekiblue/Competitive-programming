class Solution:
    def myPow(self, x: float, n: int) -> float:
        #Base Cases
        if n==0:
            return 1
        elif n == -1:
            return 1/x
        elif n==1:
            return x
        #Recursive Cases
        elif n%2 == 0:
            return self.myPow(x*x,n//2)
        else:
            return x * self.myPow(x*x,(n-1)//2)