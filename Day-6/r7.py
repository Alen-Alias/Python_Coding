def f(n):
    if n==0:
        return 200
    x=f(n-1)
    print(n,end=" ")
    return x
n=5
print(f(n))