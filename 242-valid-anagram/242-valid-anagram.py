class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        hashMap = {}
        
        for i in s:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] +=1
                
        for i in t:
            if i in hashMap:
                hashMap[i] -=1
            else:
                return False
            
        for val in hashMap.values():
            if val != 0:
                return False
        
        return True
        