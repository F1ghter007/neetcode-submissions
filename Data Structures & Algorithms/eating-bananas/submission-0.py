class Solution:
    def minEatingSpeed(self, nums: List[int], h: int) -> int:
        start,end=1,max(nums)
        ans=float('inf')
        while start<=end:
            mid=(start+end)//2
            hours=0
            for num in nums:
                hours=hours+math.ceil(num/mid)
            if hours<=h:
                ans=min(ans,mid)
                end=mid-1
            else:
                start=mid+1
        return ans