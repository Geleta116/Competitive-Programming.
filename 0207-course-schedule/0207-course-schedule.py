class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [ 0 for _ in range(numCourses)]
        
        graph = defaultdict(list)
        
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1
        
        queue = deque()
        
        for index in range(len(indegree)):
            if indegree[index] == 0:
                queue.append(index)
        
        output = []

        while queue:
            current = queue.pop()
            
            output.append(indegree)
            
            for child in graph[current]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        if len(output) == len(indegree):
            return True
        return False
        