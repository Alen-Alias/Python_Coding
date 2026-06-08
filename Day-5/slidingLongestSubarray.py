lis=list(map(int,input().split()))
k=int(input())
m,s,l,r=0,0,0,0
while(r<len(lis)):
    s+=lis[r]
    if s>k:
        s-=lis[l]
        l+=1
    m=max(m,r-l+1)
    r+=1
print(m)