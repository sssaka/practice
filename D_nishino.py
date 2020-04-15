N = int(input()) #N is the amount of A_i
l=[]
g=[]
for i in range(N):
    l.append(int(input()))
    
S=int(N*(N+1)*0.5)
b=[x for x in set(l) if l.count(x)>1]
if len(b)==1 :
    a=b[0]+(S-sum(l))
    print(b[0],a)
else:
    print('Correct')
