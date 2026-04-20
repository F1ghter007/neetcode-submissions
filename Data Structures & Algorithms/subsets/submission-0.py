class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp=[]
        ans=[]
        def rec(i):
            if i>=len(nums):
                ans.append(temp.copy())
                return
            temp.append(nums[i])
            rec(i+1)
            temp.pop()
            rec(i+1)
            return
        rec(0)
        return ans
