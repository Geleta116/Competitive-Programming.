class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        pre = defaultdict(set)
        
        indegree = defaultdict(int)
        
        graph = defaultdict(list)
        
        queue = deque()
        
        for course in prerequisites:
            graph[course[0]].append(course[1])
            indegree[course[1]] += 1
        
        for course in graph:
            if indegree[course] == 0:
                queue.append(course)
        
        while queue:
            
            curr = queue.popleft()
            
            for child in graph[curr]:
                for item in pre[curr]:
                    pre[child].add(item)
                pre[child].add(curr)
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    
        output = []
        
        for query in queries:
            
            if query[0] in pre[query[1]]:
                output.append(True)
            else:
                output.append(False)
                
        return output
            
            
                    
        
            
            
        
        
                
        