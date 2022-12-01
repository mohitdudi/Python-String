def cusisdigi(num):
    for x in num:
        if ord(x) in range(48,58):
            out=1
            continue
        else:
            out=0
    if out==1:
        print("True")
    else:
        print("False")
