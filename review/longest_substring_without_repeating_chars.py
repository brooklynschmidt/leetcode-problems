# Optimal:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        left = 0

        for right in range(len(s)):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)

            seen[s[right]] = right
            longest = max(longest, right - left + 1)

        return longest

# My first naive sol
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 # longest string length
        current_count = 0 # current counter
        start = 0 # pointer into string
        seen = {} # list of things we've seen of char -> index

        if not s:
            return 0

        while start < len(s):
            if s[start] not in seen:
                seen[s[start]] = start # store char -> index
                current_count += 1
                start += 1
            else:
                lastSeen = seen[s[start]]
                if current_count > longest:
                    longest = current_count
                # slide start to the lastSeen and over on
                start = lastSeen + 1
                current_count = 0
                seen.clear()

        if longest < current_count:
            return current_count

        return longest


