class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency_map = {}
        total = 0
        for char in s:
            if char not in frequency_map:
                frequency_map[char] = 1
            else:
                frequency_map[char] += 1
            
            if frequency_map[char] % 2 == 0:
                total += 2

        for k in frequency_map.keys():
            if frequency_map[k] % 2 > 0:
                total += 1
                break

        return total


