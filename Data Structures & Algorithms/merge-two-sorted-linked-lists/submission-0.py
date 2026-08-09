# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if both lists are sorted we iterate through both nodes simulatenously and 
        # combine them. The lists can be different size
        dummy = ListNode() # We need a dummy/tail, one to cache the start of the list
        tail = dummy # the other to add new values and follow along

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next # we don't want dummy in the output list so we return everything after it 

            