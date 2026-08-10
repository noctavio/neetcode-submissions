# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we use a hashmap to check if we already vivisited a node, if not continue iterating
            # this O(n) time, O(n) space since we need to visit every node
        #########################
        # visited = {}

        # while head:
        #    if head in visited:
        #        return True
        #    visited[head] = 1
        #    head = head.next

        # return False
        #########################
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True
        

        return False

