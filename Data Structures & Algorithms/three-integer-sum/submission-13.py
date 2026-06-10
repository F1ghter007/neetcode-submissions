class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #ans=set()
        res=[]
        nums.sort()
        n=len(nums)
        for i in range(0,n-2):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            first=nums[i]
            s=i+1
            e=n-1
            while s<e:
                temp=first+nums[s]+nums[e]
                if temp==0:
                    res.append([first,nums[s],nums[e]])
                    #ans.add((first,nums[s],nums[e]))
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
        #return [list(i) for i in ans]
        return res

        