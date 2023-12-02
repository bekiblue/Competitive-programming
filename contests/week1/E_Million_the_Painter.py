n=int(input())
canva=input()

if "MM" in canva or "CC" in canva or "YY" in canva:
    print("No")
    exit()     
if "??" in canva or canva[0]=="?" or canva[-1]=="?":
    print("Yes")
else:
    for index in range(1,len(canva)-1):
        if canva[index]=="?":
            if canva[index-1]==canva[index+1]:
                print("Yes")
                exit()
    print("No")


              


        





        

