# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # Binary Search
        # We want to keep track of the most recently found bad version
        left = 1
        right = n
        first = 0

        while left <= right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                first = middle
                right = middle - 1
            else:
                left = middle + 1
        return first


