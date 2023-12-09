test_case=int(input())
for test in range(test_case):
    b=input()
    a=b[0]
    for index in range(1,len(b)-2,2):
        a+=b[index]
    a+=b[-1]
    print(a)
    