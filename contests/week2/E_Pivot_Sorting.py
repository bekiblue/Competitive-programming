t = int(input())
for _ in range(t):
  mnm,mxm = 0,10**9
  n = int(input())
  a = list(map(int,input().split()))
  for index in range(n-1):
    cur,next = a[index],a[index+1]
    if cur > next:
      mnm = max(mnm,(cur+next+1)//2)
    elif cur < next:
      mxm = min(mxm,(cur+next)//2)
  if mnm <= mxm:
    print(mnm)
  else:
    print(-1)
 
