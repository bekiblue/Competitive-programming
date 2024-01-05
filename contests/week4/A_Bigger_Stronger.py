t=int(input())
for test in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    if len(set(a))== n:
        print("YES")
    else:
        print("NO")