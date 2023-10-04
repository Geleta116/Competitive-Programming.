import heapq

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        queue = deque()
        
        visited= set()
        indegree = defaultdict(int)
        graph = defaultdict(list)
        
        for post, pre in prerequisites:
            indegree[post] += 1
            graph[pre].append(post)
        
        output = []
        for key in range(numCourses):
            if not indegree[key]:
                queue.append(key)
        
        
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            output.append(curr)
            
            for child in graph[curr]:
                if child not in visited:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        queue.append(child)
                        
                  
        if len(visited) != numCourses:
            return []
        
        return output
        
            
        