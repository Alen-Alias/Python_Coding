def f(n):
    if n==0:    #base condition
        return
    print(n,end=" ")
    f(n-1)
n=10
f(n)