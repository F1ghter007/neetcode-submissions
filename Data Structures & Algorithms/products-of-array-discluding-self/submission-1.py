class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        lp=1
        rp=1
        n=len(nums)
        for i in range(0,n):
            lp=lp*nums[i]
            left.append(lp)
        for j in range(n-1,-1,-1):
            rp=rp*nums[j]
            right.append(rp)
        right.reverse()
        ans=[]
        for i in range(0,n):
            if i==0:
                ans.append(right[i+1])
            elif i==n-1:
                ans.append(left[i-1])
            else:
                ans.append(left[i-1]*right[i+1])
        return ans