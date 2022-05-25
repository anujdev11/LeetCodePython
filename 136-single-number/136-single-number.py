class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count={}
        for i in range(0,len(nums)):
            if nums[i] not in count:
                count[nums[i]]=1
            else:
                count[nums[i]] = count.get(nums[i])+1
        for i in count:
            if count.get(i) == 1:
                return i
            
            
        