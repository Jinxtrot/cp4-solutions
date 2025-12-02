class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i -1]:
                score += abs(ord(s[i]) - ord(s[i -1]))
        return score

"""
We iterate through the string, comparing each character with the previous one.
If the current character is different from the previous one, we calculate the absolute difference
between their ASCII values using the ord() function and add it to the total score.
"""