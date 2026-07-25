class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r=len(matrix)
        c=len(matrix[0])
        si,sj=0,0
        ei,ej=r-1,c-1
        ans=[]
        while si<=ei or sj<=ej:
            if si<=ei:
                for i in range(sj,ej+1,+1):
                    ans.append(matrix[si][i])
                si+=1
            if sj<=ej:
                for i in range(si,ei+1,+1):
                    ans.append(matrix[i][ej])
                ej-=1
            if si<=ei:
                for i in range(ej,sj-1,-1):
                    ans.append(matrix[ei][i])
                ei-=1
            if sj<=ej:
                for i in range(ei,si-1,-1):
                    ans.append(matrix[i][sj])
                sj+=1
        return ans 

        