# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        
        def dfs(node, isLeft):
            if not node:
                return 0
            lefty = dfs(node.left, True)
            righty = dfs(node.right, False)
            
            if not node.left and not node.right and isLeft:
                return node.val
            else:
                return lefty + righty
        out = dfs(root, False)
        return out
        """
        :type root: TreeNode
        :rtype: int
        """
        