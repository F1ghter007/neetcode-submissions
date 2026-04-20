from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t=defaultdict(int)
        for i in range(len(nums)):
            if t[nums[i]] != 0:
                return True
            t[nums[i]]+=1
        return False
        