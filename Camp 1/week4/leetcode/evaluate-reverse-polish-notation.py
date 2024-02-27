class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands=[]
        for token in tokens:
            if token =="+":
                operands.append(operands.pop()+operands.pop())
            elif token=="-":
                o1=operands.pop()
                o2=operands.pop()
                operands.append(o2-o1)
            elif token=="*":
                operands.append(operands.pop()*operands.pop())
            elif token=="/":
                o1=operands.pop()
                o2=operands.pop()
                operands.append(int(o2/o1))
            else:
                operands.append(int(token))
        return operands.pop()
                
                