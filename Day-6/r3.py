def f(n):
    if n==0:
        return
    print(n,end=" ")
    f(n-2)
n=10
f(n)