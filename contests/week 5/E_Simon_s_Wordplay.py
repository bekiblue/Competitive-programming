t=int(input())
for test in range(t):
    n=int(input())
    words=[]
    mxm=0
    for word in range(n):
        words.append(input())
    for char in "abcde":
            counts=[]
            for word in words:
                counts.append(2*(word.count(f"{char}"))-len(word))
            counts.sort(reverse=True)
            total=0
            count=0
            for c in counts:
                if c+total <= 0:
                    break 
                count+=1 
                total+=c
            mxm=max(mxm,count)
    print(mxm)
            



    