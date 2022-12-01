def cusisup(st):
    for x in st:
        if ord(x) in range(65,91):
            out=1
            continue
        else:
            out=0
    if out==1:
        print("True")
    else:
        print("False")
