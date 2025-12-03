from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            if stack and temperatures[stack[-1]] < temperatures[i]:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    prev_index = stack.pop()
                    result[prev_index] = i - prev_index
            stack.append(i)


        return result
    
"""
For this solution I have to learn the concept of Monotonic Stack. With 
this approach, we can efficiently keep track of the indices of the temperatures
that we haven't yet found a warmer day for. As we iterate through the list of
temperatures, we compare the current temperature with the temperature at the index
stored at the top of the stack. If the current temperature is higher, it means we've
found a warmer day for the temperature at that index. We then pop the index from the
stack and calculate the number of days until a warmer temperature by subtracting
the popped index from the current index. This process continues until the stack is
empty or the current temperature is not warmer than the temperature at the index
at the top of the stack. Finally, we push the current index onto the stack to
potentially find a warmer day for it in the future. This approach ensures that
we efficiently find the next warmer day for each temperature in a single pass
through the list, resulting in a time complexity of O(n).
"""