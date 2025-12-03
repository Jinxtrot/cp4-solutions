class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reversed_num = 0

        while x > 0:
            last_digit = x % 10
            reversed_num = reversed_num * 10 + last_digit
            x //= 10
        
        return original == reversed_num
    
"""
This solution checks if an integer is a palindrome by reversing the digits of the number
and comparing it to the original number. It first handles negative numbers by returning
False, as negative numbers cannot be palindromes. It then initializes a variable to store
the reversed number. Using a while loop, it extracts the last digit of the number using
the modulus operator, appends it to the reversed number, and removes the last digit from
the original number using integer division. Finally, it compares the reversed number to
the original number and returns True if they are the same, indicating that the number is
a palindrome, or False otherwise.
"""