class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num
        if len(str(num)) == 1:
            return num
        
        sum = 0
        
        for i in str(num):
            sum = sum + int(i)
        
        return self.addDigits(sum)
        
            
            
        