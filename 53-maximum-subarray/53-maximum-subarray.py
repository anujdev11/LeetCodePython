class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maximum=float(-inf)
        subArrSum=0
        
        for i in range(0,len(nums)):
            subArrSum+=nums[i]
            
            if subArrSum>maximum:
                maximum=subArrSum
            if subArrSum<0:
                subArrSum=0
        return maximum