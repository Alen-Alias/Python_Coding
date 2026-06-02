l=list(map(int,input().split()))
r=[]
l.sort()
for i in l:
    if i%2==0:
        r.insert(0,i)
    else:
        r.append(i)
print(r)