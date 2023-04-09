class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjecency_list = defaultdict(set)
        
        for row in range(len(isConnected)):
            for col in range(len(isConnected)):
                
                if isConnected[row][col]:
                    adjecency_list[row + 1].add(col + 1)
                    adjecency_list[col + 1].add(row + 1)
                    
        
        output = 0
        self.checked = set()
        print(adjecency_list)
        
        def dfs(province):
            self.checked.add(province)
                
            if adjecency_list[province] == []:
                return
            
            for subordinate in adjecency_list[province]:
                if subordinate not in self.checked:
                    dfs(subordinate)
                    
            return
            
        for city in adjecency_list:
            if city not in self.checked:
                output += 1
                dfs(city)
                
        return output
        
        
                    
                    
                    
                
                
            
            
            
            
            
            
        