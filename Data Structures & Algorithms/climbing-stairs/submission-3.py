class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(n,dp):
            if n==0 or n==1:
                return 1
            if dp[n]!= -1:
                return dp[n]
            dp[n] = rec(n-1,dp)+rec(n-2,dp)
            return dp[n]
        dp=[-1]*(n+1)
        return rec(n,dp)
        