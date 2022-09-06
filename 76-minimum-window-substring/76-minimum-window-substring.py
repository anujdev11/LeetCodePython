class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        s_count, t_count = Counter(), Counter(t)
        
        result = []
        
        l,r=0,0
        
        while r <= len(s)-1:
            s_count[s[r]] += 1            
            r += 1
            if s_count & t_count != t_count:
                continue
            
            while l<r:
                s_count[s[l]] -= 1
                l+=1
                
                if s_count & t_count == t_count:
                    continue
                result.append(s[l-1:r])
                break
                
        if not result:
            return ""        
        return min(result, key=len)
                