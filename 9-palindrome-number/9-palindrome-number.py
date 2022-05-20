class Solution:
    def isPalindrome(self, x: int) -> bool:
        Temp = x
        Reverse = 0
        while(x > 0):    
            Reminder = x %10    
            Reverse = (Reverse *10) + Reminder    
            x = x //10
        print(x,Reverse)
        if Temp==Reverse:
            return True
        else:
            return False