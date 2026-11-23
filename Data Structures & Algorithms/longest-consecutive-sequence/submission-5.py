class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        occ = {}
        for i in nums:
            occ[i] = 1
        vis = {}
        ans=0
        for i in nums:
            temp=0
            j=i
            while (j not in vis and j in occ):
                temp+=1
                vis[j]=1
                j=j-1
            j=i+1
            while (j not in vis and j in occ):
                temp+=1
                vis[j]=1
                j+=1
            ans=max(ans,temp)
        return ans 