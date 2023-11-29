class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        exponent = 16  
        while exponent >= 0:
            if n == 0 or n==3**exponent:
                return True
            if n > 3**exponent:
                n -= 3**exponent
            exponent -= 1 
        return False 
