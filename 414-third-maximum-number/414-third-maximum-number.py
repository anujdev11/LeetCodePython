class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort(reverse=True)
        if len(nums) == 2:
            return nums[0]
        if len(nums) == 1:
            return nums[0]
        
        return nums[2]