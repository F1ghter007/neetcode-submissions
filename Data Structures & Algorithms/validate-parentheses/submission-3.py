class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        d={'(':')','{':'}','[':']'}
        for i in s:
            if i=='(' or i=='{' or  i=='[':
                a.append(i)
            else:
                if len(a)==0:
                    return False
                p=a.pop()
                if i!=d[p]:
                    return False
        if len(a)!=0:
            return False
        return True