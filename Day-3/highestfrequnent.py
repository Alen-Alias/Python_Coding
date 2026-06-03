l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:v 
        d[i]+=1
e,m=0,0
for i in d:
    if(d[i]>m):
        m=d[i]
        e=i 
print(e)