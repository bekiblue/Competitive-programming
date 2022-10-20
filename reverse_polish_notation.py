class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands=[]
        operators=['+','-','*','/']
        for i in tokens:

            if i not in operators:
                operands.append(int(i))
            else:
                o1=operands.pop()
                o2=operands.pop()
                if i == '+':
                    operands.append(o1+o2)
                if i == '-':
                    operands.append(o2-o1)
                if i == '*':
                    operands.append(o1*o2)
                if i == '/':
                    operands.append(int(o2/o1))
        return operands.pop()
