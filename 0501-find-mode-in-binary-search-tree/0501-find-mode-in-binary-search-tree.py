# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        frequency = defaultdict(int)
        def inorder(root):
            if not root:
                return
            frequency[root.val] += 1
            inorder(root.left)
            inorder(root.right)
            
        inorder(root)
        new = []
        for key in frequency:
            new.append([frequency[key],key])
        new.sort(reverse = True)
        out = []
        for item in new:
            if item[0] == new[0][0]:
                out.append(item[1])
        return out
       