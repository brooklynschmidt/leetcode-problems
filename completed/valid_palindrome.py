class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = ''
        for char in s:
            if char.isalnum():
                cleaned_text += char.lower()
        
        # Can also use a filter
        # lower = s.lower()
        # cleaned_text = ''.join(filter(str.isalnum, lower))
        
        left = 0
        right = len(cleaned_text) - 1

        while left < right:
            if cleaned_text[left] == cleaned_text[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
