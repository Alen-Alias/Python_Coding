l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
e1,e2,m1,m2=0,0,0,0
for i in d:
    if d[i]>m1:
        m1,m2,e1,e2=d[i],m1,i,e1
    elif m2<d[i] and m1!=d[i]:
        m2,e2=d[i],i
print(e2)