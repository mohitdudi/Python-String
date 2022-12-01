def cusisalnum(st):
    for x in st:
        if ord(x) in range(65,91):
            out=1
            continue
        elif ord(x) in range(90,123):
            out=1
            continue
        elif ord(x) in range(48,58):
            out=1
            continue
        else:
            out=0
    if out==1:
        print("True")
    elif out==0:
        print("False")
