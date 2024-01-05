from collections import defaultdict 
t=int(input())
for test in range(t):
    ur_mxm=0
    ul_mxm=0
    i=-1
    j=-1
    chess=[]
    first_diagonal=defaultdict(int)
    second_diagonal=defaultdict(int)
    n,m=[int(x) for x in input().split()]
    for r in range(n):
        chess.append([int(x) for x in input().split()])
    for row in range(n):
        for col in range(m):
            first_diagonal[row+col]+=chess[row][col]
            second_diagonal[row-col]+=chess[row][col]
            
    