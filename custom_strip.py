def custrip(st):
    c=1
    while(c<=2):
        i=0
        l=len(st)
        out=""
        while(i<l):
            if(ord(st[i])==32):
                i+=1
                continue
            else:
                while(i<l):
                    out=out+st[i]
                    i+=1
                break
        st=out[::-1]
        c+=1
    out=out[::-1]
    return out