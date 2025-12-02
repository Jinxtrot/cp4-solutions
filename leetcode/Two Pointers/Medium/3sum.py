from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_numbers = sorted(nums)
        n = len(nums)
        result = []

        for i in range(len(sorted_numbers)):
            if i > 0 and sorted_numbers[i] == sorted_numbers[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                suma = sorted_numbers[i] + sorted_numbers[left] + sorted_numbers[right]

                if suma > 0:
                    right -= 1
                elif suma < 0:
                    left += 1
                else:
                    result.append([sorted_numbers[i], sorted_numbers[left], sorted_numbers[right]])

                    while left < right and sorted_numbers[left] == sorted_numbers[left + 1]:
                        left += 1
                    while left < right and sorted_numbers[right] == sorted_numbers[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1

        return result

'''
We first sort the input list to facilitate the two-pointer approach.
We iterate through the sorted list, fixing one number at a time and using two pointers to find
pairs that sum to the negative of the fixed number.
To avoid duplicates, we skip over numbers that are the same as the previous number.
When we find a valid triplet, we add it to the result list and move both pointers inward, skipping over duplicates.
This continues until all unique triplets that sum to zero are found.
'''