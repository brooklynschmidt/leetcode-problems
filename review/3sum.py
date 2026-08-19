class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting in order helps with finding the target sum quicker
        # e.g. if sum is too big, lower right pointer
        # e.g. if sum is too small, raise left pointer
        nums.sort()
        n = len(nums)
        result = []

        # 3 pointers: 1 fixed at i, one at i + 1, one at end of list
        for i in range(n - 2):
            # no longer possible to find any matches since a positive nums[i] requires negative values
            # left & right pointers are ahead of i, so this is not possible
            if nums[i] > 0:
                break
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            # end when left and right cross to prevent seeing duplicates
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # too low
                if total < 0:
                    left += 1
                # too high
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return result
