class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[[0]*9 for i in range(9)]
        col=[[0]*9 for i in range(9)]
        box=[[0]*9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if row[i][int(board[i][j])-1]!=0 or col[j][int(board[i][j])-1]!=0 or box[(i//3)*3+(j//3)][int(board[i][j])-1]!=0:
                    return False
                    continue
                row[i][int(board[i][j])-1]=1
                col[j][int(board[i][j])-1]=1
                box[(i//3)*3+(j//3)][int(board[i][j])-1]=1
        print(row)
        print(col)
        print(box)
        return True