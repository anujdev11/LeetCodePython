class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n==4:
            return False
        
        suma = 0
        for i in str(n):
            i = int(i)
            suma = suma + (i*i)   
        n = suma
        return Solution.isHappy(self,n)
        

            
        