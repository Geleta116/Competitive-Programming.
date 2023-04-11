class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        adjecency_list = defaultdict(list)
        
        for dislike in dislikes:
            adjecency_list[dislike[0]].append(dislike[1])
            adjecency_list[dislike[1]].append(dislike[0])
        
        self.out = True
        self.colored = defaultdict(int)
        
        def dfs(current, parentGroup):
            if parentGroup == 0:
                
                self.colored[current] = 0
                for item in adjecency_list[current]:
                    if item in self.colored:
                        if self.colored[item] != 1:
                            self.out = False
                            return
                    else:
                        dfs(item, 1)
            
            else:
                
                
                self.colored[current] = 1
                for item in adjecency_list[current]:
                    if item in self.colored:
                        if self.colored[item] != 0:
                            self.out = False
                            return
                    else:
                        dfs(item, 0)
            
            return 
        
        
        for item in adjecency_list:
            if item not in self.colored:
                dfs(item, 0)
            
        return self.out
                