class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=float('-inf')
        maxs=float('-inf')
        for i in nums:
            curr=max(curr+i,i)
            maxs=max(maxs,curr)
        return maxs