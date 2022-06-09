class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        
        if len(nums) == 1:
            return nums[0]
        
        for i in range(0,len(nums)):
            if nums[i] in hashMap.keys():
                hashMap[nums[i]] += 1
                if hashMap[nums[i]] > len(nums)/2:
                    return nums[i]   
            else:
                hashMap[nums[i]] = 1
                
                
        