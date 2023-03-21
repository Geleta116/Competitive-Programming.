# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)
        for node in range(1, len(preorder)):
            newnode = TreeNode(preorder[node])
            if not stack or stack[-1].val > newnode.val:
                stack[-1].left = newnode
                stack.append(newnode)
            else:
                while stack and stack[-1].val < newnode.val:
                    popped = stack.pop()
                popped.right = newnode
                stack.append(newnode)
                
        return root