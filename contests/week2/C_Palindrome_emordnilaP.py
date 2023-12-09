t=int(input())
for test in range(t):
    n=int(input())
    a=input().split()
    for index in range(n):
        digit=a[index]
        left=index
        right=n-1
        exist=False
        while right >= left+2:
            if a[right] == digit:
                exist=True
                break
            right-=1
        if exist :
            break
    if exist :
        print("YES")
    else:
        print("NO")
    
        
    