l=input().split()
r=[]
for i in l:
    if(l.count(i)%2==1 and i not in r):
        r.append(i)
print(r)