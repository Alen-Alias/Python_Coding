n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    temp =l[len(l)-1]
    l.pop()
    l.insert(0,temp)
print(l)


"""
n=int(input())
l=list(map(int,input().split()))
temp=l[-1]
for i in range(len(l)-1,0,-1):
    l[i]=[i-1]
l[0]=temp
print(l)
"""