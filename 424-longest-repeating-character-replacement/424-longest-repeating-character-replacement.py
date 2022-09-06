class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        count=0
        cFrequency = {}
        
        for r in range(len(s)):
            
            if s[r] not in cFrequency:
                cFrequency[s[r]] = 1
            cFrequency[s[r]]+=1
        
            if (r-l+1) - max(cFrequency.values()) < k:
                count = max(count,r-l+1)                
            else:
                cFrequency[s[l]]-=1
                l+=1
        
        return count
            
                
            
            
                
        
                
        