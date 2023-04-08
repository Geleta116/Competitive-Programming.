"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.max_depth = 0
        
        if not root:
            return 0
        
        def dfs(root, depth):
            if len(root.children) == 0:
                self.max_depth = max( self.max_depth, depth)
                return
            
            for arr in root.children:
                dfs(arr, depth + 1)
        
        dfs(root, 1)
        return self.max_depth
                