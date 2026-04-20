class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp=len(nums)
        for i in range(temp):
            nums[nums[i]%temp-1]+=temp
        for i in range(temp):
            if nums[i]//temp > 1:
                return i+1