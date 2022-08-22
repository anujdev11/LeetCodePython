class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        if len(height) == 2:
            return(min(height[0],height[1]))
            
        
        i=0
        j=len(height)-1
        
        maxLen = -1
        maxWater = -1
        while i<j:
            if height[i]==height[j]:
                maxWater = max(maxWater,min(height[i],height[j])*(j-i))
                i+=1
            elif height[i]<=height[j]:
                maxWater = max(maxWater,min(height[i],height[j])*(j-i))
                i+=1
            else:
                maxWater = max(maxWater,min(height[i],height[j])*(j-i))
                j-=1
            
                
        return maxWater
            
            
        
        