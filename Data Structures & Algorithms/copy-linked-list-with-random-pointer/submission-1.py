"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #headCopy = Node(head.val, head.next, head.random)
        
        #curr = headCopy.next
        #while curr is not None:
        #    newNode = Node(curr.val, curr.next, curr.random)
        #    curr = curr.next

        oldToCopy = {None:None} #needs to map null for an edge case
        curr = head
        while curr is not None:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head 
        while curr is not None:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]
