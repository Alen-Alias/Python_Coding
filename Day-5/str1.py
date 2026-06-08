s=input()
res=""
now=s[0]
count=1
for i in range(1,len(s)-1):
    if now==s[i]:
        count+=1
    else:
        res+=now+str(count)
        now=s[i]
        count=1
res+=now+str(count)
print(res)
