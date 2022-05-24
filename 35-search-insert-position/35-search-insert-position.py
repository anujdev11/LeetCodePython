class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       
        if nums[0] == target:
            return 0
        start = 0
        end  = len(nums)-1
        
        if nums[end]<target:
            return end+1
        
        if nums[start]>target:
            return start
        
        while start<=end:
            mid = (start+end)//2
            if nums[mid] == target and nums[mid-1]<target:
                return mid
            elif nums[mid] <target:
                start = mid + 1
            else:
                end = mid -1
            if nums[mid] != target and nums[mid]>target and nums[mid-1]<target:
                return mid
        return -1
        
        