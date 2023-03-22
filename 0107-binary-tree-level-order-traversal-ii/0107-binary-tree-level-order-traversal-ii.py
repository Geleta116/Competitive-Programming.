# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = defaultdict(list)
        def travers(root, parent):
            if not root:
                return
            levels[parent - 1].append(root.val)
            travers(root.left, parent - 1)
            travers(root.right, parent - 1)
        
        travers(root, 0)
        new =  sorted(levels.items())
        output = []
        for item in new:
            output.append(item[-1])
        return output
            
        
        