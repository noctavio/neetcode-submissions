# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        # the r
        queue = collections.deque()
        queue.append(root)

        while queue:
            rightOrVisible = None
            for n in range(len(queue)): 
                # level order traversal, we keep overwriting rightSide, on the final overWrite 
                    # it will be the right node
                node = queue.popleft()
                if node:
                    rightOrVisible = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightOrVisible is not None:
                result.append(rightOrVisible.val)

        return result
            