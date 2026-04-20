class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[]
        post=[]
        prod1=1
        prod2=1
        for i in range(len(nums)):
            prod1*=nums[i]
            pre.append(prod1)
        for i in range(len(nums)-1,-1,-1):
            prod2*=nums[i]
            post.append(prod2)
        post.reverse()
        ans=[]
        for i in range(len(nums)):
            if i==0:
                ans.append(post[i+1])
            elif i==len(nums)-1:
                ans.append(pre[i-1])
            else:
                ans.append(pre[i-1]*post[i+1])
        return ans
        