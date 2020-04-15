x=int(input())
n=int(input())
for i in range(x-1):
    m=n
    n=int(input())
    a=n-m
    if a>0:
        print("up "+str(a))
    elif a<0:
        print("down "+str(-a))
    else:
        print("stay")
