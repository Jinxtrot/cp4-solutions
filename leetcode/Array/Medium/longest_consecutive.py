class Solution:
    def longestConsecutive(self,nums:list[int])->int:
        nums=sorted(nums)
        print(nums)
        longest_streak = 0
        current_streak = 0
        previous_num = -10**9 - 20
        start_over = True
        for num in nums:
            if start_over:
                current_streak = 1
                start_over = False
            if num == previous_num + 1:
                current_streak += 1
            elif num == previous_num:
                continue
            else:
                longest_streak = max(longest_streak, current_streak)
                start_over = True
            previous_num = num
        longest_streak = max(longest_streak, current_streak)
        return longest_streak
    
'''
First we sort the input list.
Then we iterate through the sorted list, keeping track of the current streak of consecutive numbers.
If the current number is one more than the previous number, we increment the current streak.
If the current number is the same as the previous number, we continue to the next iteration.
If the current number is not consecutive, we compare the current streak with the longest streak found so far and reset the current streak.
Finally, we return the longest streak found.
'''
    


