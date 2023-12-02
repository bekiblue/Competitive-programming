test_case=int(input())
nums=list(map(int,input().split()))
even=[]
odd=[]
for num in nums:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
if len(odd)%2==0:
    print(sum(even)+sum(odd))
else:
    odd.sort()
    print(sum(even)+(sum(odd)-odd[0]))