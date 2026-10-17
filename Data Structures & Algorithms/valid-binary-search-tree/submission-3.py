# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(curr, left, right):
            if curr is None:
                return True

            # if not within the boundary 
            if not(curr.val < right and curr.val > left):
                return False
            
            # recursively explore left subtree using [left, curr.val] boundary 
                # as well as right subtree using [currRoot, right] boundary
            return (valid(curr.left, left, curr.val) and
            valid (curr.right, curr.val, right))
        return valid(root, float("-inf"), float("inf"))