from collections import Counter
t=int(input())
for test in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    freq=Counter(a)
    for num in freq:
        if freq[num]==1:
            print(a.index(num)+1)
            break
                  
