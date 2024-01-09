from collections import defaultdict,Counter
t=int(input())
for test in range(t):
    n=int(input())
    s=input()
    follow=defaultdict(list)
    check=False
    for char in range(n-1):
        if  s[char+1] in follow[s[char]]:
            if s[char+1]==s[char] and char!=0 and s[char]==s[char-1]:
                if Counter(follow[s[char]])[s[char]]>1:
                    check=True
                    break
                else:
                    follow[s[char]].append(s[char+1])
                    continue
            else:
                check=True
                break        
        else:
            follow[s[char]].append(s[char+1])
    if check:
        print("YES")
    else:
        print("NO")
