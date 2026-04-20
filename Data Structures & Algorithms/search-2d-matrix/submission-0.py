class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])
        l,r=0,row-1
        while l<r:
            m=(l+r)//2
            if (target<matrix[m][col-1]):
                r=r-1
            elif(target>matrix[m][col-1]):
                l=l+1
            else:
                return True
        if l==r:
            sl,sr=0,col-1
            while sl<=sr:
                m=(sl+sr)//2
                if(target>matrix[l][m]):
                    sl=sl+1
                elif(target<matrix[l][m]):
                    sr=sr-1
                else:
                    return True
        return False