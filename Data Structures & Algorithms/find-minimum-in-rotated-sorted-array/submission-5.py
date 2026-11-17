class Solution:
    def findMin(self, nums: List[int]) -> int:
        start,end = 0,len(nums)-1
        n=len(nums)
        while start<=end:
            mid= start + (end-start)//2
            if nums[mid]<nums[(mid+n-1)%n] and nums[mid]<nums[(mid+1)%n]:
                return nums[mid]
            elif nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid-1
        return nums[mid]