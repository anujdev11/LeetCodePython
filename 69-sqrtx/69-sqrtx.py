import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        ans  = math.sqrt(x)
        return int(ans)