class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        stack = set()
        
        for num in nums:
            if num in stack:
                stack.remove(num)
            else:
                stack.add(num)
        if len(stack) == 0:
            return True
        