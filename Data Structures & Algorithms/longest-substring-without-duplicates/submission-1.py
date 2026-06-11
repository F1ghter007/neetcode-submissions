
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        i=0
        j=0
        ans=0
        n=len(s)
        while j<n:
            if (d.get(s[j],0)==0):
                d[s[j]]=d.get(s[j],0)+1
                ans=max(ans,j-i+1)
                j+=1
            else:
                d[s[i]]=d.get(s[i],0)-1
                i+=1
        return ans
                