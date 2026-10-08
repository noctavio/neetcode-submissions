# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(currNode, maxVal):
            if currNode is None:
                return 0
            
            if currNode.val >= maxVal:
                result = 1
            else:
                result = 0
            
            maxVal = max(maxVal, currNode.val)
            result += dfs(currNode.left, maxVal)
            result += dfs(currNode.right, maxVal)
            return result

        return dfs(root, root.val)


        

        
        
