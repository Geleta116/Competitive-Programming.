class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        #This function is used to check if the frequency is smaller
        def binary(query,words, mid):
            if query < words[mid]:
                return True
            return False
                
            
            
           
        
        
            
        #this function is used to convert the provided string to the frequency of the
        # lexicographically smallest characyer
        def count_minimum(word):
            word = list(word)
            word.sort()
            count = word.count(word[0])
            return count
        
        
        
        
        #this converts the query array to an array of numbers
        # which are the frequencies of the lexicographically smallest number
        for query in range(len(queries)):
            queries[query] = count_minimum(queries[query])
        
        
        
        
        
        #this converts the query array to an array of numbers
        # which are the frequencies of the lexicographically smallest number
        for word in range(len(words)):
            words[word] = count_minimum(words[word])
        
        words.sort()
        
        
        
        #THIS IS THE BINARY SEARCH PART FOR THE QUERIES
        for i, query in enumerate(queries):
            
            start = -1
            end = len(words)
            while end > start + 1:
                mid = start + (end - start) // 2
                
                if binary(query,  words, mid):
                    end = mid
                else:
                    start = mid
        
            queries[i] = len(words) - end 
        
        return queries
            
                    
                
        
        
        