from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i]:
                    return False
                row[i].append(board[i][j])
                if board[i][j] in col[j]:
                    return False
                col[j].append(board[i][j])
                if board[i][j] in box[i//3,j//3]:
                    return False
                box[i//3,j//3].append(board[i][j])
        return True

                
        