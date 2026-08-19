class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        # Voting Algorithm
        # The intuition here is that if we see the same number more than once, we increase the count
        # If we see a different number, we decrease the count
        # If the count reaches 0, we switch to the newly seen number
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
            if count <= 0:
                candidate = nums[i]
                count += 1
        
        return candidate
        
        