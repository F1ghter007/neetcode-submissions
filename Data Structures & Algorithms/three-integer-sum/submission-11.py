class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        n=len(nums)
        for i in range(0,n-2):
            first=nums[i]
            s=i+1
            e=n-1
            while s<e:
                temp=first+nums[s]+nums[e]
                if temp==0:
                    ans.add((first,nums[s],nums[e]))
                    s+=1
                    e-=1
                elif temp>0:
                    e-=1
                elif temp<0:
                    s+=1
        return [list(i) for i in ans]

        