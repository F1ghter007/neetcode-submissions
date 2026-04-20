class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])
        vis = set()
        ops = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(i,j):
            count=0
            
            if min(i,j)<0 or i>=row or j>=col or (i,j) in vis or grid[i][j] == 1:
                return 0
            if i==row-1 and j==col-1:
                return 1
            vis.add((i,j))
            for k in range(4):
                count += dfs(i+ops[k][0] , j+ops[k][1])
            vis.remove((i,j))
            return count
        return dfs(0,0)

        