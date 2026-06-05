n=int(input())
l=list(map(int,input().split()))

def rotate(i,j,l):
    while(i<j):
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1
    return l


n=n%len(l)
l=rotate(0,len(l)-1,l)
l=rotate(0,n-1,l)
l=rotate(n,len(l)-1,l)
print(l)