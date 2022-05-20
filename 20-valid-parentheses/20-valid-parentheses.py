class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        paranthesis={'(':')', '{':'}', '[':']'}
        if len(s) % 2 != 0:
            return False
        
        for i in s:
            if i in paranthesis.keys():
                res.append(i)
            else:
                if res==[]:
                    return False
                a = res.pop()
                if i!=paranthesis[a]:
                    return False
        if res==[]:
            return True
        else:
            return False
        