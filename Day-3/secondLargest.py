l=list(map(int,input().split()))
m1,m2=0,0
for i in l:
    if m1<i:
        m1,m2=i,m1
    elif m2<i and m1!=i:
        m2=i
print(m2)