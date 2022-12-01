# Custom lower function ===>>>> cuslw

def cuslw(st):
    for x in st:
        if ord(x) in range(97,123):
            print(x,end="")
        else:
            y=ord(x)+32
            x=chr(y)
            print(x,end="")

