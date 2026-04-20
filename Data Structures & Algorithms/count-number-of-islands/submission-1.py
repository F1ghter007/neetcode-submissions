from collections import deque;
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        row,col = len(grid),len(grid[0])
        ans=0

        def check(i,j):
            return (0<=i<row) and (0<=j<col) and grid[i][j] == "1"
        
        def dfs(r,c):
            ops = [[0,1],[1,0],[0,-1],[-1,0]]
            # que = deque()
            # que.append((r,c))
            grid[r][c] = "0"
            # while que:
            #     i,j = que.popleft()
            #     grid[i][j] = "0"
            for k in range(4):
                tempr,tempc = r+ops[k][0],c+ops[k][1]
                if check(tempr,tempc):
                    dfs(tempr,tempc)
                    grid[tempr][tempc] = "0"


        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ans+=1
        return ans
