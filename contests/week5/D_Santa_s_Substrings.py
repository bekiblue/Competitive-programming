n=int(input())
#bubble sorting
words=[]
for word in range(n):
    words.append(input())
possible=True
for cycle in range(n):
    swapped=False
    for index in range(n-1):
        if words[index] in words[index+1]:
            continue
        elif words[index+1] in words[index]:
            words[index],words[index+1]=words[index+1],words[index]
            swapped=True
        else:
            possible=False
            break
    if possible and not swapped:
        print("YES")
        break
    if not possible:
        print("NO")
        exit()
for word in words:
    print(word)
