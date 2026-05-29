class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i in range(0,len(nums)):
            if a.get(target-nums[i],-1)!=-1:
                return [a[(target-nums[i])],i]
            a[nums[i]]=i
