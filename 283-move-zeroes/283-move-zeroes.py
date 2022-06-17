class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 and nums[0]:
            return nums
        
        count = 0
        j = 0
        k=len(nums)-1
        for i in range(0,len(nums)):
            if nums[i] == 0:
                count+=1
            else:
                nums[j] = nums[i]
                j=j+1
        for l in range(count):
            nums[k] = 0
            k=k-1
                
        