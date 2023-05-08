class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        checker = defaultdict(int)
        
        for item in recipes:
            checker[item] = 1
      
        for index, ingridient in enumerate(ingredients):
            for each in ingridient:
                graph[each].append(recipes[index])
                indegree[recipes[index]] += 1
            
        
        queue = deque()
        
        for supply in supplies:
            queue.append(supply)
        output = []
        
        while queue:
            
            current = queue.popleft()
            
            if current in checker:
                output.append(current)
            
            for child in graph[current]:
                indegree[child] -= 1
                
                if indegree[child] == 0:
                    queue.append(child)
                    
        return output
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        