s=input()
a=s.split(' ')
N=int(len(a))
for i in range(1,N-1):
    h=i+1
    if int(a[h])-int(a[i])>0:
        print('up',str(int(a[h])-int(a[i])))
    elif int(a[h])-int(a[i])==0:
        print('stay')
    else:
        print('down',str(-int(a[h])+int(a[i])))
        
