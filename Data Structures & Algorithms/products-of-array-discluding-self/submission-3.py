class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forw = []
        back =[1 for i in range(len(nums))]
        temp=1
        for i in nums:
            forw.append(i*temp)
            temp=i*temp
        temp=1
        for i in range(len(nums)-1,-1,-1):
            back[i]=temp*nums[i]
            temp = nums[i]*temp
        for i in range(len(nums)):
            nums[i]= (forw[i-1] if i>0 else 1) * (back[i+1] if i+1<len(nums) else 1)
        #print (back)
        return nums