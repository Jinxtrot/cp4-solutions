class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] in dict:
                return([dict[target-nums[i]],i])
            dict[nums[i]]=i
        return []

'''
This code goes through the list of numbers while creating a dictionary with the numbers as keys and their indices as values.
It checks if the complement (target - current number) exists in the dictionary. If it does, it returns the indices of the two numbers that add up to the target.
If no such pair is found, it returns an empty list.
This solution has a time complexity of O(n) and a space complexity of O(n) due to the dictionary used for storing indices.
'''
