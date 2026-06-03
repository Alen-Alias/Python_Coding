l=list(map(int,input().split()))
i=len(l)//2
j=0
while(i<len(l)//4):
    l[i], l[len(l)-j-1] = l[len(l)-j-1] ,l[i]
    i+=1
    j+=1
print(l)
