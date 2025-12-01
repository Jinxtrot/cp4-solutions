from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}

        for number in nums:
            if number not in numbers:
                numbers[number] = 1
            else:
                numbers[number] += 1
        
        sorted_numbers = sorted(numbers.items(), key=lambda item: item[1], reverse=True)
        print(sorted_numbers)
        
        top_k_elements = [key for key,value in sorted_numbers[:k]]

        return top_k_elements

