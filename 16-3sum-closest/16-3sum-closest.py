class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        res = nums[0] + nums[1] + nums[2]
        for i in range(0,len(nums)-2):
            left,right = i+1,len(nums)-1
            while left<right:
                
                sum = nums[i]+nums[left]+nums[right]
                
                if sum == target:
                    return sum
                if abs(sum - target) < abs(res - target):
                    res = sum
                if sum<target:
                    left+=1
                else:
                    right-=1
        return res