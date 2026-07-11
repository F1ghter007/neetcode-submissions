class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=len(nums)
        ans=float('inf')
        k=0
        temp=0
        for i in range(l):
            temp+=nums[i]
            while temp>=target:
                ans=min(i-k+1,ans)
                temp-=nums[k]
                k+=1
        if ans==float('inf'):
            return 0
        return ans
        