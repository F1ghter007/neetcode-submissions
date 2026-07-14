class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        l=len(nums)
        nums.sort()
        for i in range(0,l-1):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            s=i+1
            e=l-1
            while s<e:
                temp=nums[i]+nums[s]+nums[e]
                if temp==0:
                    res.append([nums[i],nums[s],nums[e]])
                    s+=1
                    e-=1
                    while s<e and nums[s]==nums[s-1]:
                        s+=1
                    while s<e and nums[e]==nums[e+1]:
                        e-=1
                elif temp>0:
                    e-=1
                elif temp<0:
                    s+=1
        return res
        