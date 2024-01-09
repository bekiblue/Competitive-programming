t=int(input())
follow={ "Y":"e","e":"s","s":"Y"}
for test in range(t):
    s=input()
    check=True
    if s[-1] not in "Yes":
        print("NO")
        continue
    for char in range(len(s)-1):
        if follow.get(s[char]) != s[char+1]:
            check=False
            break

    if check:
        print("YES")
    else:
        print("NO")
