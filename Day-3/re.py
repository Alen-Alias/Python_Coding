l=list(map(int,input().split()))
i=0
while i<(len(l)//2):
    l[i],l[len(l)-i-1]=l[len(l)-1-i],l[i]
    i+=1
print(l)