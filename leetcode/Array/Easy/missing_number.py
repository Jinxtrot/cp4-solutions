class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        final_list = [-1 for i in range(len(nums) + 1)]
        for num in nums:
            final_list[num] = num
        for i in range(len(final_list)):
            if final_list[i] == -1:
                return i
        return -1

'''
My solution creates a temporary list initialized with -1 with the length of the input list plus one.
It then iterates through the input list, marking the indices corresponding to the numbers present in the input list.
Finally, it checks the temporary list for the first index that still has -1, which indicates the missing number.
This solution has a time complexity of O(n) and a space complexity of O(n) due to the additional list used for tracking the numbers.
'''