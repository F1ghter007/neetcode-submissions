class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for i in magazine:
            d[i]=d.get(i,0)+1
        for i in ransomNote:
            if d.get(i,0)<=0:
                return False
            d[i]-=1
        return True