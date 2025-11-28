from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            order_word = ''.join(sorted(word))

            if order_word not in anagrams:
                anagrams[order_word] = []
            anagrams[order_word].append(word)

        return list(anagrams.values())
    

    """
    This solution groups anagrams by sorting each word to create a unique key for each group.
    Since anagrams consist of the same letters, sorting them will yield the same result.
    It uses a dictionary to map these sorted keys to lists of anagrams.
    The time complexity is O(n * k log k), where n is the number of words and k is the maximum length of a word,
    due to the sorting operation for each word.
    """


