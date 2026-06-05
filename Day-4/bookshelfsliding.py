l=list(map(int,input().split()))
k=int(input())
max=sum(l[:k])
s=max
for i in range(1,len(l)-k+1):
    s=s-l[i-1]+l[i+k-1]
    if s>max:
        max=s
print(max)