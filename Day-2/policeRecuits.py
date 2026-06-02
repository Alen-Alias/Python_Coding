n=int(input())
events=list(map(int,input().split()))
r=0;
miss=0
for i in events:
    if i>0:
        r+=i
    elif r>0:
        r-=1
    else:
        miss+=1
print(miss)
    