# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        start_head = ListNode(0)
        current = start_head
        total = 0

        while l1 or l2 or carry:
            first_number = l1.val if l1 else 0
            second_number = l2.val if l2 else 0

            total = first_number + second_number + carry
            carry = total // 10
            result_digit = total % 10

            current.next = ListNode(result_digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return start_head.next
    

"""
In this solution I learned to make linked list in python and how to traverse them.
The solution is pretty simple since it just obtains the values from the two linked lists,
adds them while keeping track of the carry, and constructs a new linked list in reverse order to represent the sum.
"""
            



