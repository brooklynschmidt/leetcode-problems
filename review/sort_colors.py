class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        idx = 0

        for color in range(3):
            freq = count.get(color, 0)
            nums[idx : idx + freq] = [color] * freq
            idx += freq

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        r = len(nums) - 1
        mid = 0

        while mid <= r:
            if nums[mid] == 0:
                nums[mid], nums[l] = nums[l], nums[mid]
                l += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[r] = nums[r], nums[mid]
                r -= 1
        return nums


