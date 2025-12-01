from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_array = sorted(nums)

        previous_value = -10**6 - 1
        current_streak = 0
        max_streak = 0

        for number in sorted_array:
            if number == previous_value + 1:
                current_streak += 1
                previous_value = number
            elif number == previous_value:
                continue
            else:
                max_streak = max(current_streak,max_streak)
                current_streak = 1
                previous_value = number
        return max(current_streak, max_streak)


"""
This is a straightforward solution that sorts the array first and then iterates through it to find the longest consecutive sequence.
We iterate through the sorted array, checking if the current number is consecutive to the previous one. If it is, we increase the current streak count.
If it's a duplicate, we skip it. If it's not consecutive, we compare the current streak with the maximum streak found so far and reset the current streak.
Time complexity: O(n log n) due to sorting
Space complexity: O(1) if we don't count the space used by sorting
"""