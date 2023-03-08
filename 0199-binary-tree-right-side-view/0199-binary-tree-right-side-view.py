# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        levels = defaultdict(list)
        if not root:
            return  []
        queue.append([root,1])
        
        while queue:
            node,curr = queue.popleft()
            levels[curr].append(node.val)
            if node.left:
                queue.append([node.left ,curr + 1])
            if node.right:
                queue.append([node.right,curr + 1])
        out = []
        for keys in levels:
            out.append(levels[keys][-1])
        return out
        