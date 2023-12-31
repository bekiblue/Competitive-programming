class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            digits=[]
            for digit in str(num):
                digits.append(digit)
            min_index=0
            for index in range(1,len(digits)):
                if digits[index]!="0" and digits[index] < digits[min_index]:
                    min_index=index
            digits[0],digits[min_index]=digits[min_index],digits[0]
            for slow in range(1,len(digits)):
                min_index=slow
                for fast in range(slow+1,len(digits)):
                    if digits[fast]<digits[min_index]:
                        min_index=fast
                digits[slow],digits[min_index]=digits[min_index],digits[slow]
            num=int("".join(digits))
        else:
            digits=[]
            for digit in str(-num):
                digits.append(digit)
            max_index=0
            for index in range(1,len(digits)):
                if digits[index]!="0" and digits[index] > digits[max_index]:
                    max_index=index
            digits[0],digits[max_index]=digits[max_index],digits[0]
            for slow in range(1,len(digits)):
                max_index=slow
                for fast in range(slow+1,len(digits)):
                    if digits[fast] > digits[max_index]:
                        max_index=fast
                digits[slow],digits[max_index]=digits[max_index],digits[slow]
            num=-int("".join(digits))
        return num
        