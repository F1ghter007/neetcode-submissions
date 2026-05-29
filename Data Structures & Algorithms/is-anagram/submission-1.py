class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a={}
        b={}
        for i,j in zip(s,t):
            a[i]=1+a.get(i,0)
            b[j]=1+b.get(j,0)
        if a==b:
            return True
        return False
            
        