class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters_index = {}
        left = 0
        max_length = 0

        for current in range(len(s)):
            if s[current] in letters_index and letters_index[s[current]] >= left:
                left = letters_index[s[current]] + 1

            letters_index[s[current]] = current
            max_length = max(max_length, (current + 1) - left)

        return max_length

"""
In this solution, I make a hash map to store the last seen index of each character.
With that I can maintain a sliding window using two pointers (left and current) to track the longest substring without repeating characters.
When a repeating character is found within the current window, I move the left pointer to one position after the last occurrence of that character.
This approach ensures that each character is processed only once, resulting in an O(n) time complexity.
"""

        