t=int(input())
for test in range(t):
    n,m=list(map(int,input().split()))
    desires=list(map(int,input().split()))
    desires.sort(reverse=True)
    needed=2*desires[0]+sum(desires[1:n-1])+n
    if needed > m:
        print("NO")
    else:
        print("YES")
    

