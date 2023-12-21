class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for digit in range((len(digits))-1,-1,-1):
            if digits[digit] != 9:
                digits[digit]+=1
                digits=digits[:digit+1]+([0]*(len(digits)-digit-1))
                break
        else:
            digits=[1]+[0]*len(digits)

        return digits