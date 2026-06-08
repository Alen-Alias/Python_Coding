"""def d(n,c=0):
    if n==1:
        return c
    elif n%2==0:
        c=d(n//2,c+1)
    else:
        c=min(d(n+1,c+1),d(n-1,c+1))
    return c

n=int(input())
print(d(n))"""


def d(n):
    if n==1:
        return 0
    elif n%2==0:
        return 1+d(n//2)
    else:
        return 1+min(d(n+1),d(n-1))

n=int(input())
print(d(n))