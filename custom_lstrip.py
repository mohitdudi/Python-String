def cuslst(st):
    i=0
    while i<len(st):
        x=st[i]
        if ord(x)==32:
            i+=1
            continue
        else:
            while(i<len(st)):
                x=st[i]
                print(x,end="")
                i+=1
            break
        i+=1
