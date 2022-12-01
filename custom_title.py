def custe(st):
    list=st.split()
    for st in list:
        if (ord(st[0]) in range(65, 91)):
            print(st[0], end="")
        elif (ord(st[0]) in range(97, 123)):
            y = ord(st[0]) - 32
            print(chr(y), end="")
        i=1
        while(i<len(st)):
            x=st[i]
            if(ord(x) in range(97,123)):
                print(x,end="")
            elif(ord(x) in range(65,91)):
                x=ord(x)+32
                print(chr(x),end="")
            elif(ord(x) not in (range(65,91) or range(90,123))):
                print(x,end="")
            i+=1
        print(" ",end="")
