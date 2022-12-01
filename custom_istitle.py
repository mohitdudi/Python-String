def cusistitle(st):
    def custe(st):
        out=""
        list=st.split()
        for st in list:
            if (ord(st[0]) in range(65, 91)):
                out=out+st[0]
            elif (ord(st[0]) in range(97, 123)):
                y = ord(st[0]) - 32
                out=out+chr(y)
            i=1
            while(i<len(st)):
                x=st[i]
                if(ord(x) in range(97,123)):
                    out=out+x
                elif(ord(x) in range(65,91)):
                    x=ord(x)+32
                    out=out+chr(x)
                elif(ord(x) not in (range(65,91) or range(90,123))):
                    out=out+x
                i+=1
            out=out+" "
        return out
        
    t=custe(st)
    print(t)
    print(st)
    if (st+" "==t):
        return True
    else:
        return False
        
