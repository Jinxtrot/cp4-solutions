from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]
        
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
        
        return answer
    

"""
This is the first problem that I haved to watch a video explanation for.
The idea is to use two passes to calculate the prefix and suffix products without using extra space for them.
The first pass calculates the prefix products and stores them in the answer array, the prefix product is in short words
the product of all elements to the left of the current index.
The second pass calculates the suffix products in reverse order and multiplies them to the corresponding index in the answer array,
the suffix product is the product of all elements to the right of the current index
Time complexity: O(n)Space complexity: O(1) (excluding the output array)
"""