class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         
#         hashMap = {}
#         for i in range(0,len(numbers)):
#             remaining = target-numbers[i]
#             if remaining in hashMap:
#                 return [hashMap[remaining],i+1]
#             else:
#                 hashMap[numbers[i]] = i+1


        left = 0
        right = len(numbers)-1
        
        while left<right:
            if numbers[left]+numbers[right] < target:
                left+= 1
            else:
                if numbers[left]+numbers[right]==target:
                    return [left+1,right+1]
                right-=1
                
        
        
                
      
            
        