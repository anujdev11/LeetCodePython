class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # s="pwwkew"
        
        lastSeen={}        
        maxLength=0
        l,r=0,0
        
        for r in range(len(s)):
            if s[r] in lastSeen:
                l = max(l,lastSeen[s[r]]+1)
                
            maxLength = max(maxLength,r-l+1)
            lastSeen[s[r]] = r
        
        return maxLength
        
            