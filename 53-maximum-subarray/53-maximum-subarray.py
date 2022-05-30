class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        suma=0
        maxa=-100000
        for i in range(len(nums)):
            suma+=nums[i]
            if suma>=maxa:
                maxa=suma   
            if suma<0:
                suma = 0
        return maxa
            
        