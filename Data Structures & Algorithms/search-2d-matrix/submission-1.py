class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sr=0
        en=len(matrix)-1
        if target<matrix[0][0]:
            return False
        while sr<=en and sr>=0:
            if target==matrix[sr][0]:
                return True
            if target<matrix[sr][0]:
                sr=sr-1
                break
            else:
                sr+=1
        if sr==len(matrix):
            sr-=1
        print(sr)
        start=0
        end=len(matrix[0])-1
        while start<=end:
            mid=start+(end-start)//2
            val=matrix[sr][mid]
            if val==target:
                return True
            if val>target:
                end=mid-1
            else:
                start=mid+1
        return False
        