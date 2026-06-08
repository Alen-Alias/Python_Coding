"""def f(n,i):
    if i>n:
        return
    print(i,end=" ")
    f(n,i+1)
    if i!=n:
        print(i,end=" ")
n=10
f(n,1)"""

def f(n,i):
    if i==n:
        return
    print(i+1,end=" ")
    f(n,i+1)
    if i+1!=n:
        print(i+1,end=" ")
n=10
f(n,0)