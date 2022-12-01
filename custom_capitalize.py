def cuscap(st):
    x=st[0]
    if ord(x) in range(65,91):
        print(x,end="")
    elif ord(x) in range(90,123):
        y=ord(x) - 32
        print(chr(y),end="")
    i=1
    while(i<len(st)):
        a=st[i]
        if ord(a) in range(90,123):
            print(a,end="")
        elif ord(a) in range(65,91):
            b=ord(a)+32
            print(chr(b),end="")
        i+=1

