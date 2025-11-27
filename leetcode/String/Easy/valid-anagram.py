class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_in_word = {}
        letters_in_comparison = {}
        for char in s:
            if char in letters_in_word:
                letters_in_word[char] += 1
            else:
                letters_in_word[char] = 1
        
        for char in t:
            if char in letters_in_comparison:
                letters_in_comparison[char] += 1
            else:
                letters_in_comparison[char] = 1

        if letters_in_word == letters_in_comparison:
            return True
        else:
            return False

"""
I created two dictionaries to count the occurrences of each character in both strings.
Then, I compared the two dictionaries. If they are equal, the strings are anagrams; otherwise, they are not.
The time complexity is O(n), where n is the length of the longer string, since we need to iterate through both strings once.
"""
