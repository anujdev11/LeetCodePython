class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap.keys():
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
        allValues = list(hashMap.values())
        for i in allValues:
            if i > 1: 
                return True
        return False
        
            
        