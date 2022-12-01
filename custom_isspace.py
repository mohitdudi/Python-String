def cusispace(st):
    for x in st:
        if ord(x)==32:
            out=1
            continue
        else:
            out=0
    if out==1:
        print("True")
    else:
        print("False")
