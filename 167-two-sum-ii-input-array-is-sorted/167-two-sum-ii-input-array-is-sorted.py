class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        hashMap = {}
        
        for i in range(0,len(numbers)):
            
            remaining = target-numbers[i]
            
            if remaining in hashMap:
                return [hashMap[remaining],i+1]
            
            else:
                hashMap[numbers[i]] = i+1
                
            
        