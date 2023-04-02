# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        checker = defaultdict(list)
        def bfs(root, row):
            if not root:
                return
            checker[row].append(root.val)
            bfs(root.left, row + 1)
            bfs(root.right, row + 1)
        bfs(root, 0)
        return checker[len(checker) - 1][0]
            
            
        