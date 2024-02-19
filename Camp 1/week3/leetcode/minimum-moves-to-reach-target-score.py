class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        operations=0
        num=target
        while num > 1 and maxDoubles > 0 :
            if num%2 == 0:
                num=num//2 
                operations+=1
                maxDoubles-=1
            else:
                num-=1
                operations+=1
        if num > 1:
            operations+=(num-1) 
        return operations
        