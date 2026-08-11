class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        if n==2:
            return 1
        f,s,t=0,1,1
        a=0
        for i in range(3,n+1):
            a=f+s+t
            f,s,t=s,t,a
        return a
        