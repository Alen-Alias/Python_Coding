n=int(input())
v=list(map(int,input().split()))
a=list(map(int,input().split()))
c=[0]*(max(v))

for i in range(n):
    if a[i]>=18:
        c[v[i]-1]+=1

ctemp =sorted(c,reverse = True)
if ctemp[0]==ctemp[1]:
    print(-1)
else:
    print(c.index(ctemp[0])+1)