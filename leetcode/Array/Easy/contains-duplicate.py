from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        else:
            return False
        
"""
I make a set of the items in the List. If the length of each one is different that means that 
there are duplicates in the List.
"""
