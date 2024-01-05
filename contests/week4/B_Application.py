from collections import defaultdict 
t=int(input())
database=defaultdict(int)
for test in range(t):
    name=input()
    if database[name]==0:
        print("OK")
    else:
        print(f"{name}{database[name]}")
    database[name]+=1