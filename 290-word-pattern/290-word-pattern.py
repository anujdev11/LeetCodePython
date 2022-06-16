class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        newStr = s.split(" ")

        hashMap={}
        if len(pattern)!=len(newStr):
            return False
        else:
            for i in range(0,len(newStr)):
                if pattern[i] not in hashMap and newStr[i] not in hashMap.values():
                    hashMap[pattern[i]] = newStr[i]
        
                if pattern[i] not in hashMap.keys() or newStr[i] != hashMap[pattern[i]]:
                    return False
        return True          
                    
            
        