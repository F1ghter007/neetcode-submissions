class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        vis={}
        count=0
        for i in nums:
            dic[i]=1
        for i in nums:
            temp=0
            if vis.get(i,0) == 0 and vis.get(i-1,0) == 0:
                curr=i
                while dic.get(curr,0) > 0:
                    vis[curr] = 1
                    temp+=1
                    curr=curr+1
                count=max(count,temp)
            
        return count
        