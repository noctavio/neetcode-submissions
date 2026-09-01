# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if curr is None: 
                return [True, 0]

            left = dfs(curr.left)
            right = dfs(curr.right)

            childrenBalanced = (left[0] and right[0])
            heightBalanced = abs(left[1] - right[1]) <= 1

            subtreeBalanced = childrenBalanced and heightBalanced

            return [subtreeBalanced, max(left[1], right[1]) + 1]

        isBalanced, height = dfs(root)
        return isBalanced