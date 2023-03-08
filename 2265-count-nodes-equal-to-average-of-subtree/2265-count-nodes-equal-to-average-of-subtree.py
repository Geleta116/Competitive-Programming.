# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def average(root):
            if not root:
                return (0,0)
            curr_l_summ,curr_l_size = average(root.left)
            curr_r_summ,curr_r_size = average(root.right)
            
            summ = root.val + curr_l_summ + curr_r_summ
            size = 1 + curr_r_size + curr_l_size
            if summ //  size == root.val:
                self.count += 1
            return (summ,size) 
        average(root)
        return self.count
        