from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            current_height = min(height[left], height[right])
            current_width = right - left
            current_area = current_height * current_width
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    

'''
We use a two-pointer approach to find the maximum area of water that can be contained.
We initialize two pointers, one at the beginning (left) and one at the end (right) of the height list.
We calculate the area formed between the two pointers and update the maximum area if the current area is larger.
We then move the pointer pointing to the shorter line, as moving the taller line would not increase the area.
This process continues until the two pointers meet.
'''