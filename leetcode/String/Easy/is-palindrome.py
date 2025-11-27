class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        cleaned = ''.join(char for char in s if char.isalnum()).lower()
        right = len(cleaned) - 1
        print(cleaned)


        while left < right: 
            if cleaned[left] == cleaned[right]:
                left += 1
                right -= 1
                continue
            else:
                return False
            
        return True
    
'''
This solution first cleans the input string by removing non-alphanumeric characters and converting it to lowercase.
Then, it uses two pointers to compare characters from the start and end of the cleaned string, moving towards the center.
If all corresponding characters match, the function returns True, indicating that the string is a palindrome; otherwise, it returns False.
'''
