from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum > target:
                right -= 1 
            if sum < target:
                left += 1
            if sum == target:
                return [left + 1,right+1]
            
"""
This solution was easy due to the sorted array. Once we have it sorted, we just need to compare if the sum is greater
or lower than the target. If the sum is lower, we increase the left pointer and if it is greater we reduce the right pointer.
Once we have the sum equal to the target, we can now have the indexes responsible for the sum.
This solution is O(n) and don't use any extra space.
"""
