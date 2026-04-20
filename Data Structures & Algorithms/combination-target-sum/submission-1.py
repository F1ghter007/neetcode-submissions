class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp=[]
        ans=[]
        def rec(i,t):
            if t>target:
                return
            if t==target:
                if temp.copy() not in ans:
                    ans.append(temp.copy())
                return
            if i>=len(nums):
                return 
            temp.append(nums[i])
            rec(i,t+nums[i])
            #rec(i+1,t+nums[i])
            temp.pop()
            rec(i+1,t)
            return
        rec(0,0)
        return ans
        