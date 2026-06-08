def wildfire(m,i,j):
    if i<0 or i>len(m)-1 or j<0 or j>len(m[0])-1 or m[i][j]!=1:
        return
    m[i][j]=2
    wildfire(m,i-1,j)
    wildfire(m,i+1,j)
    wildfire(m,i,j-1)
    wildfire(m,i,j+1)

m = [[1,1,1,1],
    [1,0,0,0],
    [0,0,1,1],
    [1,1,0,0]]
wildfire(m,0,0)
count=0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j]==1:
            count+=1
print(count)