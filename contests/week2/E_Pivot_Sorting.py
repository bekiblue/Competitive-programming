t = int(input())
for _ in range(t):
  left,right = 0,10**9
  n = int(input())
  a = list(map(int,input().split()))
  for index in range(n-1):
    x,y = a[index],a[index+1]
    if x > y:
      left = max(left,(x+y+1)//2)
    elif x < y:
      right = min(right,(x+y)//2)
  if left <= right:
    print(left)
  else:
    print(-1)