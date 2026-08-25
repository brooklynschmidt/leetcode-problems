class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)

        total = int((length * (length + 1)) / 2)
        
        for i in nums:
            total -= i
        
        return total
