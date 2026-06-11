class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l,m=0,1
        ans=0
        while m<n and l<n:
            if prices[m]<prices[l]:
                l=m
                m=m+1
            else:
                ans=max(ans,prices[m]-prices[l])
                m+=1
        return ans

