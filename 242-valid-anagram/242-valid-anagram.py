class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(t) < len(s):
            return False
        
        for i in s:
            if i in t:
                t = t.replace(i,"",1)
           
        if t == "":
            return True
        else:
            return False
        