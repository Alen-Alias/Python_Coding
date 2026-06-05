l=list(map(int,input().split()))
k=int(input())
max=0
for i in range(0,len(l)-k):
    s=sum(l[i:i+k])
    if max<s:
        max=s
print(max) 