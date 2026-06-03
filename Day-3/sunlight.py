l=list(map(int,input().split()))
c=0
max=0
for i in l:
    if max<l[i]:
        c+=1
        max+=1
print(c)
