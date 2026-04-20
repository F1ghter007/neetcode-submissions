class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        n=len(nums)
        nums.sort()
        d=[]
        for i in range(n-2):
            if nums[i]>0:
                break
            st=i+1
            en=i+2
            while (i!=st and st!=en and en!=i) and i<n and st<n and en<n:
                temp=nums[i]+nums[st]+nums[en]
                if temp<0:
                    st+=1
                    en+=1
                elif temp>0:
                    st-=1
                else:
                    l1=[nums[i],nums[st],nums[en]]
                    if l1 not in d:
                        d.append(l1)
                    st+=1
                    en+=1
        return d
        # if len(nums)<3:
        #     return []
        # first=0
        # second=1
        # last=len(nums)-1
        # d=[]
        # nums.sort()
        # while (first!=second and second!=last and first!=last) and (first<len(nums) and last<len(nums) and second<len(nums)):
        #     temp=nums[first]+nums[second]+nums[last]
        #     if temp==0:
        #         c=[nums[first],nums[second],nums[last]]
        #         if c not in d:
        #             d.append(c)
        #         if(second>=0):
        #             last-=1
        #         else:
        #             first+=1
        #             second+=1
        #     elif temp>0:
        #         last-=1
        #     elif temp<0:
        #         first+=1
        #         second+=1
        # return d
        

        
        
        # if len(nums)<3:
        #     return []
        # first=0
        # second=1
        # last=len(nums)-1
        # d=[]
        # nums.sort()
        # while (first!=second and second!=last and first!=last) and (first<len(nums) and last<len(nums) and second<len(nums)):
        #     temp=nums[first]+nums[second]+nums[last]
        #     if temp==0:
        #         c=[nums[first],nums[second],nums[last]]
        #         if c not in d:
        #             d.append(c)
        #         if(second>=0):
        #             last-=1
        #         else:
        #             first+=1
        #             second+=1
        #     elif temp>0:
        #         last-=1
        #     elif temp<0:
        #         first+=1
        #         second+=1
        # return d
        

        