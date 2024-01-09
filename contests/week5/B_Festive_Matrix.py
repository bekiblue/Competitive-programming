matrix=[]
n=int(input())
for row in range(n):
    matrix.append(list(map(int,input().split())))
total=0
for row in range(n):
    for col in range(n):
        if row==(n-1)//2 or col==(n-1)//2 or row==col or row+col==n-1:
            total+=matrix[row][col]
print(total)
