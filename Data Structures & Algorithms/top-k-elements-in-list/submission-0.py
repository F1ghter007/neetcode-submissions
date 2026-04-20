class Solution:
    def topKFrequent(self, nums: List[int], t: int) -> List[int]:
        count=[[] for i in range(len(nums)+1)]
        res={}
        for i in nums:
            res[i]=res.get(i,0)+1
        for a,b in res.items():
            count[b].append(a)
        ans=[]
        for i in range(len(count)-1,-1,-1):
            for k in count[i]:
                ans.append(k)
                if len(ans)==t:
                    return ans

        