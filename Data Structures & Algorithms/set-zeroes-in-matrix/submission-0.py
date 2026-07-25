class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        rm={}
        cm={}
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rm[i]=1
                    cm[j]=1
        for i in range(r):
            for j in range(c):
                if (i in rm) or (j in cm):
                    matrix[i][j]=0
                    