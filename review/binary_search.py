class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            half = (left + right) // 2
            if nums[half] == target:
                return half
            elif nums[half] < target:
                left = half + 1
            else:
                right = half - 1
        
        return -1
