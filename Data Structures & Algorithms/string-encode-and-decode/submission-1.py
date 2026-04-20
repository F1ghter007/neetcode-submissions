class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res+=str(len(i))+"#"+i
        #print(res)
        return res

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            l=int(s[i:j])
            ans.append(s[j+1:j+1+l])
            i=j+l+1
        return ans