# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # at the most fundemental the problem is asking you to construct an integer
        # from a linked list. One entire linked list reps ONE number 

        # So return the head of the new linked list that is the sum of those two values

        # We should try to reverse these linked lists because the leading number is at the
        # end. If we don't reverse we will have to use O(n) space to store visited values
        # to later consturct the integer value coressponding with the list

        # once they are reversed 

        # WE DONT REVERSE!!!!
        result = ListNode()
        curr = result

        carry = 0
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            
            digit = val1 + val2 + carry
            carry = digit // 10
            digit = digit % 10
            curr.next = ListNode(digit)

            curr = curr.next 
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else: 
                l2 = None
        return result.next
