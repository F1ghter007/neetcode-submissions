class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        sl,tl=len(s),len(t)
        if sl!=tl:
            return False
        for i in range(sl):
            if d1.get(s[i],-1)==-1 and d2.get(t[i],-1)==-1:
                d1[s[i]]=t[i]
                d2[t[i]]=s[i]
            elif d1.get(s[i],-1)!=-1 and d2.get(t[i],-1)!=-1:
                if d1[s[i]]==t[i] and d2[t[i]]==s[i]:
                    continue
                else:
                    return False
            else:
                return False
        return True