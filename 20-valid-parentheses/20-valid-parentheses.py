class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        
        hashMap={'(':')','[':']','{':'}'}
        
        for i in s:
            if i in hashMap.keys():
                stack.append(i)
            else:
                if stack==[]:
                    return False
                a = stack.pop()
                if i!=hashMap[a]:
                    return False
            
        if stack==[]:
            return True
        else:
            return False
        
        