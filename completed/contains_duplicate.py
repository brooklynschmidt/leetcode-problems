class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Converting to a set gets rid of duplicates, so lengths will differ
        return len(nums) > len(set(nums))

        # Optionally, can use a frequency map
