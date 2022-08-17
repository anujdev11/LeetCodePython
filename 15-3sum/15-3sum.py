class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()
        print(nums)
        
        for i in range(0,len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            left,right = i+1,len(nums)-1
            
            
            while left<right:
                s = nums[i]+nums[left]+nums[right]
                
                if s == 0:
                    res.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif s<0:
                    left+=1
                else:
                    right-=1
        return list(res)
                    
                
                
                
            
            
            
            
        
        
        
#         res = []
#         nums = [-2,0,1,1,2]
#          k=2
#         for i in range(len(nums)):
#             for j in range(1,len(nums)):
#                 print(i,j,k)
#                 if nums[i]+nums[j]+nums[k]==0 and i!=j and i != k and j != k:
#                     result = []
#                     result.append(nums[i])
#                     result.append(nums[j])
#                     result.append(nums[k])
#                     result = sorted(result)
#                     if result not in res:
#                         res.append(result)
#                 if k < len(nums)-1:
#                     k += 1
#         return res

    

#         res = []
#         hashMap = {}
#         for i in range(len(nums)):
#             for j in range(1,len(nums)):
#                 k=j+1
#                 remaining = 0 - nums[i]-nums[j]      
#                 if remaining in hashMap and i != j and i != k and j != k:
#                     result = []
#                     result.append(nums[i])
#                     result.append(nums[j])
#                     result.append(remaining)
#                     result = sorted(result)
#                     if result not in res:
#                         res.append(result)
#                 if k < len(nums)-1:
#                     k += 1
                    
#                 else:
#                     if remaining in nums:
#                         hashMap[remaining] = i 
#         return res
                
    
                
        