st=input("Enter a string: ")
for x in st:
    if ord(x) in range(65,91):
        print(x,end="")
    else:
        y=ord(x)-32
        x=chr(y)
        print(x,end="")

