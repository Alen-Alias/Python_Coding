l=input().split()
l.sort()
for i in l:
    if l.count(i)>1:
        while(l.count(i)!=1):
            l.remove(i)
print(l)

# order is different after removing