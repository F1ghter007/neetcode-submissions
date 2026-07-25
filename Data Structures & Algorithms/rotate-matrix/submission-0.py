class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r//2):
            for j in range(c):
                matrix[i][j],matrix[r-i-1][j] =matrix[r-i-1][j],matrix[i][j]
        for i in range(r):
            for j in range(c):
                if i<j:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]