class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        
        
        nums.sort()
        
        
        sol_1 = nums[-1]*nums[-2]*nums[-3]
        
        sol_2 = nums[-1]*nums[0]*nums[1]
        
        return max(sol_1,sol_2)
            
        