from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        row,col = len(grid) , len(grid[0])
        length=0
        q = deque()
        visit = [[0 for i in range(col)] for j in range(row)]
        q.append((0,0))
        visit[0][0] = 1
        ops = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                if x == row-1 and y == col-1:
                    return length
                for j in range(4):
                    xn , yn = x + ops[j][0] , y + ops[j][1]
                    if (min(xn,yn)<0 or xn>=row or yn>=col or visit[xn][yn]==1 or grid[xn][yn] == 1):
                        continue
                    q.append((xn,yn))
                    visit[xn][yn]=1

            length+=1
        return -1
        