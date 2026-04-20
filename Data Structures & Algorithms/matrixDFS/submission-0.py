class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        self.count=0
        ops = [[0,1],[0,-1],[1,0],[-1,0]]
        row = len(grid)
        col = len(grid[0])
        vis = [[0 for i in range(col)] for j in range(row)]
        def dfs(i,j,vis):
            if min(i,j) < 0 or i>=row or j>=col or vis[i][j]==1 or grid[i][j] == 1:
                return 0
            if i==row-1 and j==col-1:
                return 1
            vis[i][j]=1
            temp=0
            for z in range(4):
                temp+= dfs(i+ops[z][0],j+ops[z][1],vis)
            vis[i][j]=0
            return temp
            #return self.count
        return dfs(0,0,vis)
        