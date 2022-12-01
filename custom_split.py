def cusplit(st,ar):
    lt=[]
    w=""
    for c in st:
        if ord(c)!=ord(ar):
            w=w+c
        elif ord(c)==ord(ar):
            lt=lt+[w]
            w=""
    lt.append(w)
    print(lt)
