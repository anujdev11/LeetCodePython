class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        
        # nums = [5,7,7,8,8,10]
        
        start = 0
        end = len(nums)-1
        res=[]
        
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
                break
        for j in reversed(range(len(nums))):
            if nums[j] == target:
                res.append(j)
                break
        if len(res)==0:
            return [-1,-1]
        
        return res
        
                
        