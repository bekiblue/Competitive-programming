test_case=int(input())
count=0
word="codeforces"
for test in range(test_case):
    count=0
    s=input()
    for index in range(10):
        if s[index]!=word[index]:
            count+=1
    print(count)
    
    
