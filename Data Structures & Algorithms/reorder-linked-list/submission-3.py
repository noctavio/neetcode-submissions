# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
                            # do a single pass of the linked list
                                # a pointer to the respective node using the pattern as the key
                                # 0, n-1, 1, n-2, 2, n-3

        # optimal approach is a two pointer one
        # we have a pointer at the start of the LinkedList
        # another at the end
        left = head 
        right = head.next

                    #if right.next is None: #two nodes, initialize and then it's sorted
                    #    return head

                    #while right.next.next is not None: 
                    #    if right.next is not None and right.next.next is None: # odd case one last move
                    #        left = left.next
                    #        right = right.next
                    #        break

                    #    left = left.next # even case continue traversing until condition fails
                    #    right = right.next.next

        while right and right.next:
            left = left.next
            right = right.next.next
        
        second = left.next
        prev = None
        left.next = None

        # reverse
        while second is not None:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge
        first, second = head, prev
        while second is not None:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        
        # this is a simple approach connect left node ptr to right node ptr
        # then move left +=1 (next) and right -= 1 (also next) 
            #### how is it next? because we're going to reverse the right half of the LinkedList 
            # it must be reversed since there's no prev ptr in a singly linkedlist

        
            # my idea for finding the half, pass through the list reach the and count how many nodes 
            # integer division that value count again get to the half, then apply reversal on the 2nd half

            # now just append left than right move ptrs left right, until both next ptrs are null 
        
        # the optimal way is to use a fast/slow ptr, when fast.next is null or fast is null we know
        # then our slow ptr should always land in the first half, meaning slow.next will be the start of 
        # 2nd half which needs a reversal applied
            