class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        flag = 0
        for i in range(len(nums)):
            if nums[i] in hashMap.keys():
                hashMap[nums[i]] += 1
                flag = 1
            else:
                hashMap[nums[i]] = 1
        if flag == 1: 
            return True
        else:
            return False
        
            
        