class Solution:
    def isHappy(self, n: int) -> bool:
        generated=set()
        while n not in generated:
            generated.add(n)
            if n==1:
                return True
            num=str(n)
            n=0
            for digit in num:
                n+=int(digit)**2

        return False



