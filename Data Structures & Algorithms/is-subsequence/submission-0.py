class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j,se,te=0,0,len(s),len(t)
        while i<se and j<te:
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i==se:
            return True
        return False