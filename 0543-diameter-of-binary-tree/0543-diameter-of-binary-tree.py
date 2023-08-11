# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def all(nodes):
            output = 1
            def dfs(node):
                if not node:
                    return 0
                curr = max(dfs(node.left), dfs(node.right))
                return curr + 1

            h1 = dfs(nodes.left)
            h2 = dfs(nodes.right)
            output += h1 + h2 -1
            self.out = max(self.out, output)
            return output
        
        self.out = 0
        def traverse(node):
            if not node:
                return 
            all(node)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return self.out