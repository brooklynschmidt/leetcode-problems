class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store a hash-map of numbers we have seen
        sums = {}

        for i in range(len(nums)):
            # Constantly looking in our hash-map for the target value
            find = target - nums[i]
            if find in sums:
                return [i, sums[find]]
            else:
                sums[nums[i]] = i
        
