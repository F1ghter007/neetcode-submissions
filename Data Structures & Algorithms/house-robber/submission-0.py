class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        def rec(n):
            if n>=len(nums):
                return 0
            if n in dp:
                return dp[n]
            dp[n]=max(nums[n]+rec(n+2),rec(n+1))
            return dp[n]
        return rec(0)