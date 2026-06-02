n=int(input())
t=n
digits=0
if n==0:
    digits=1
while n>0:
    digits+=1
    n//=10
n=t
x=0
while n>0:
    x+=(n%10)**digits
    n//=10
if x==t:
    print("Armstrong")
else:
    print("Not Armstrong")
    