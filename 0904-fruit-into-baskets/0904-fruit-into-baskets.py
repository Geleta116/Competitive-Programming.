class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        checker = {}
        answer = 0
        start = 0
        
        for tree in range(len(fruits)):
            if fruits[tree] in checker :
                checker[fruits[tree]] += 1
            else:
                checker[fruits[tree]] = 1
            
            while len(checker)>2:
                
                if checker[fruits[start]] == 1:
                    del checker[fruits[start]]
                    start += 1
                    
                else:
                    checker[fruits[start]] -= 1
                    start += 1
            answer = max(answer, tree - start + 1)
                
        return answer
    
                        
                        
                    
                    
                
            
        
        