"""def f(n,i):
    if i>n:
        return
    print(i,end=" ")
    f(n,i+2)
n=10
f(n,2)"""

def f(n):
    if n==0:    #base condition
        return
    f(n-2)
    print(n,end=" ")
n=10
f(n)