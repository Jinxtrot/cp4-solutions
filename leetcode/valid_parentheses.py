class Solution:
    def validParentheses(self, input: str) -> bool:
        valid = {"(" : ")", "{": "}", "[":"]"}
        order = []

        for char in input:
            if char in valid.keys():
                order.append(char)
            if char in valid.values():
                if len(order)==0 or valid[order.pop()] != char:
                    return False
        return True if len(order) == 0 else False
    
'''
This solution checks if the parentheses in the input string are valid by using a stack-like approach with a list.
It iterates through each character in the input string, 
adding opening parentheses to the stack and checking if closing parentheses match the last added opening parenthesis.
If all opening parentheses are matched correctly, the function returns True; otherwise, it returns False.
'''

