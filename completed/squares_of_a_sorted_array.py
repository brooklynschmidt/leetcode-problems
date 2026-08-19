class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sorted = [0] * n
        sorted_pointer = n - 1
        left = 0
        right = n - 1

        # Two pointers, one at end and beginning of array, one pointer at end of resulting array
        while left <= right:
            # Check abs to get the highest of two
            if abs(nums[left]) > abs(nums[right]):
                # Store at END of new resulting array
                sorted[sorted_pointer] = nums[left] * nums[left]
                left += 1
                sorted_pointer -= 1
            else:
                # Store at END of new resulting array
                sorted[sorted_pointer] = nums[right] * nums[right]
                right -= 1
                sorted_pointer -= 1

        return sorted



        
