class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        if len(height) == 2:
            return(min(height[0],height[1]))
            
        
        i=0
        j=len(height)-1
        
        res = 0
        while i<j:
            if height[i]<=height[j]:
                maxWater = height[i]*(j-i)
                i+=1
            else:
                maxWater = height[j]*(j-i)
                j-=1
            
            if maxWater>res:
                res=maxWater
        return res
            
            
        
        