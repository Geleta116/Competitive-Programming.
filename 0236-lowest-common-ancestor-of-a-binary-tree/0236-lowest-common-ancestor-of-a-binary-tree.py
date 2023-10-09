# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.out = root
        
        def dfs(node):
            temp = node.val
            if not node:
                return []
            
            if not node.right and not node.left:
                
                if node == p or node == q:
                    # print("1", node.val)
                    return [node]
                
                return []
            
            left =[]
            right = []
            if node.left:
                left = dfs(node.left)
                if left and (node == p or node == q):
                    self.out = node
                    return []
            if node.right:
                right =  dfs(node.right)
                if right and (node == p or node == q):
                    self.out = node
                    return []
            if left and right:
                self.out = node
                return []
            
            if node == p or node == q:
                return [node]
            
            return left + right
        dfs(root)
        
        return self.out
                
        