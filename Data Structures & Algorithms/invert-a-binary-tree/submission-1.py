# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # the tree can be empty (no nodes)
        # values range from (-100 to 100)
            # This is a recursion problem find the base case and build a solution that applies to the 
            # remainder the of the tree
        
        if root is None:
            return root
        
        temp = root.left 
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root





            
