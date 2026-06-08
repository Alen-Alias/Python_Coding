def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

n=5
print(fib(n))
"""
Recursion tree for fib(5):

                fib(5)
              /       \
          fib(4)     fib(3)
         /    \      /    \
     fib(3) fib(2) fib(2) fib(1)
     /  \   /  \  /  \
 fib(2) fib(1)fib(1)fib(0) fib(1)
 /  \
fib(1) fib(0)

"""