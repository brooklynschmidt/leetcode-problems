class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_freq = {}
        if len(ransomNote) > len(magazine):
            return False

        # Frequency map for magazine
        for char in magazine:
            if char in mag_freq:
                mag_freq[char] += 1
            else:
                mag_freq[char] = 1

        # Iterate through ransomnote, if not in hash or hash value 0, return false
        for char in ransomNote:
            if char in mag_freq:
                if mag_freq[char] > 0:
                    mag_freq[char] -= 1
                else:
                    return False
            else:
                return False
        return True
        
