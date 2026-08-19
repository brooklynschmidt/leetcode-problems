class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Use a frequency map to count the character counts in s
        s_freq = {}
        for char in s:
            if char in s_freq:
                s_freq[char] += 1
            else:
                s_freq[char] = 1

        # if a character is in t, subtract by one
        # all chars should be 0 in the frequency table by the end to show that they have the same amount per char
        for char in t:
            if char in s_freq:
                s_freq[char] -= 1
            else:
                return False

        # max value should be 0 to be a valid anagram, otherwise a character was not decremented
        if max(s_freq.values()) != 0:
            return False
        else:
            return True
        
