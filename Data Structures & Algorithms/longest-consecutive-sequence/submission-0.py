class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        count=0
        for i in nums:
            dic[i]=1
        for i in nums:
            temp=0
            while dic.get(i,0) > 0:
                temp+=1
                i=i+1
            count=max(count,temp)
        return count
        