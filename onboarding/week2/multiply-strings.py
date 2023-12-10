class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0" :
            return "0"
        result = [0]*(len(num1)+len(num2))
        num1,num2=num1[::-1],num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                product=int(num1[i])*int(num2[j])
                result[i+j]+=product
                carry=result[i+j]//10
                result[i+j+1]+=carry
                digit=result[i+j]%10
                result[i+j]=digit
        result=result[::-1]
        start=0
        for index in range(len(result)):
            if result[index]:
                start=index
                break
        result=[str(digit) for digit in result[start:]]
        return "".join(result)
        
