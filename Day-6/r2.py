"""def f(n,i):
    if i>n:
        return
    print(i,end=" ")
    f(n,i+1)
n=5
f(n,1)"""

def f(n):
    if n==0:    #base condition
        return
    f(n-1)
    print(n,end=" ")
n=5
f(n)