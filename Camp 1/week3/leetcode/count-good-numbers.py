class Solution:
    def countGoodNumbers(self, n: int) -> int:
        five_power=(n+1)//2
        four_power=n//2
        return (self.exponential(5,five_power)*self.exponential(4,four_power)) % (10**(9)+7)      

    def exponential(self,base,power):
            #Base Case 
            if power==1:
                return base 
            elif power==0:
                return 1
            #Recursive Cases
            elif power%2 == 0 :
                return self.exponential(base*base % (10**9+7),power//2)
            else:
                return base * self.exponential(base*base % (10**9+7) ,(power-1)//2)

