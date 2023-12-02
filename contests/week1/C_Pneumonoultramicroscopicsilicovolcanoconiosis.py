test_case=int(input())
for test in range(test_case):
    word=input()
    if len(word)>10 :
        print(f"{word[0]}{len(word)-2}{word[-1]}")
    else:
        print(word)
 