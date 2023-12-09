t=int(input())
for test in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    freq={}
    count=0
    for index in range(n):
        freq[a[index]-index]=freq.get(a[index]-index,0)+1
    for value in freq.values():
        count+=((value*(value-1))//2)
    print(count)

