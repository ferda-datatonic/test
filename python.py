n = 3
matrix = [[0]*n for _ in range(n)]

def dfs(matrix,i,j,count):
    if (i >= len(matrix)) or (i<0) or (j>=len(matrix[0])) or (j<0) or matrix[i][j] != 0:
        return

    matrix[i][j] = count
    count +=1
    #in any case, we DO NOT want to go right
    #until j+1 is within i
    if j+1>=i:
        dfs(matrix,i,j+1,count)
    dfs(matrix,i+1,j,count)
    dfs(matrix,i,j-1,count)
    dfs(matrix,i-1,j,count)
dfs(matrix,i=0,j=0,count=1)
print(matrix)