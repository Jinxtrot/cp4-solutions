from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        
        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
        

"""
This solution merges two sorted arrays into one sorted array and then calculates the median.
It uses two pointers to traverse both arrays, appending the smaller element to the merged array until one array is exhausted.
After merging, it checks if the total length is odd or even to compute the median accordingly.
The time complexity is O(m + n), where m and n are the lengths of the two arrays.
"""