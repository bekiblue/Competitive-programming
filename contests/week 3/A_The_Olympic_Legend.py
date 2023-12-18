t=int(input())
for test in range(t):
    distances=[int(x) for x in input().split()]
    count=0
    for index in range(1,len(distances)):
        if distances[index] > distances[0]:
            count+=1
    print(count)
