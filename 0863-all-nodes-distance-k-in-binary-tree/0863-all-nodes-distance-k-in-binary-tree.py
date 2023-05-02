# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(root):
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                dfs(root.left)
            
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                dfs(root.right)
        dfs(root)
        
        queue = deque()
        visited = set()
        output = []
        
        queue.append((target.val,0))
        visited.add(target.val)
        while queue:
            curr, level = queue.popleft()
            if level == k :
                output.append(curr)
            if level > k :
                break
            for child in graph[curr]:
                if child not in visited:
                    visited.add(child)
                    queue.append((child, level + 1))

        return output
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
            
            
        