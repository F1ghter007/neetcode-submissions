class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        def rec(n):
            if n>=len(cost):
                return 0
            if n in dp:
                return dp[n]
            dp[n]=cost[n]+min(rec(n+1),rec(n+2))
            return dp[n]
        return min(rec(0),rec(1))
        