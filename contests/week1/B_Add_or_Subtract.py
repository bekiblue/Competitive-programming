test_case=int(input())
for test in range(test_case):
    nums=list(map(int,input().split())) 
    if nums[0]+nums[1]==nums[2]:
      print("+")
    else:
       print("-")
 