class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(i,dp):
            if i<0:
                return 0
            if i==0:
                return 1
            if dp[i]!=-1:
                return dp[i]
            dp[i]=rec(i-1,dp)+rec(i-2,dp)
            return dp[i]
        dp=[-1]*(n+1)
        return rec(n,dp)
