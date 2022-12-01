#rstrip

def cusrst(st):
    i=len(st)-1
    out=""
    while i>=0:
        x=st[i]
        if ord(x)==32:
            i-=1
            continue
        else:
            while(i>=0):
                x=st[i]
                out=out+x
                i-=1
            break
        i-=1
    out=out[::-1]
    return out
        
