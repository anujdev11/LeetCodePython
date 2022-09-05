class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res=[1]*len(nums)
        
#         for i in range(0,len(nums)):
#             product=1
#             for j in range(0,len(nums)):
#                 if i==j:
#                     continue
#                 product*=nums[j]
#             res.append(product)
#         return res

        
        prefix = 1
    
        for i in range(0,len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix*=nums[i]
            
        return res
            