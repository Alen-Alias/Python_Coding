def maze(m,path,i,j,n):
    if i==n and j==n:
        print(path)
        return
    if i+1<=n and m[i+1][j]==1:
        maze(m,path+"D",i+1,j,n)
    if j+1<=n and m[i][j+1]==1:
        maze(m,path+"R",i,j+1,n)

m=[[1,1,0,1],
[1,1,0,1],
[0,1,0,0],
[1,1,1,1]]
n=len(m)-1
maze(m,"",0,0,n)