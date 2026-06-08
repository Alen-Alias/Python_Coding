def f(n,i):
    if i>n:
        return
    print(i,end=" ")
    f(n,i+1)
    if i!=n:
        print(i,end=" ")
n=10
f(n,1)