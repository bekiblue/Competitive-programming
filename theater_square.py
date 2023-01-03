    def calc(n,a):
        if n%a == 0:
            return n//a
        else:
            return n//a + 1
     
    n,m,a=[int(x) for x in input().split()]
    width=calc(n,a)
    length=calc(m,a)
    print(width * length)
