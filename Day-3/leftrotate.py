n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    temp =l[0]
    l.pop(0)
    l.append(temp)
print(l)

"""
n=int(input())
l=list(map(int,input().split()))
temp=l[0]
for i in range(len(l)-1):
    l[i]=l[i+1]
l[-1]=temp
print(l)
"""