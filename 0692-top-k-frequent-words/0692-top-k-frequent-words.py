class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
            lexico = []
            heapq.heapify(lexico)
            output = []
            count = Counter(words)
            values = [(-count[word], word) for word in count ]
            
            heapq.heapify(values)
            current = []
            while k > 0:
                current.append(heapq.heappop(values)[1])
                k -= 1
            
#             values = list(current)
            
#             heapq.heapify(values)
#             self.count = 0
#             while len(values) > 0:
                
#                 currCount, curr = heapq.heappop(values)
#                 if currCount != self.count:
                    
#                     while len(lexico) > 0:
#                         output.append(heapq.heappop(lexico))
                        
#                 self.count = currCount
#                 heapq.heappush(lexico, curr)
                    
#             while len(lexico) > 0:
#                 output.append(heapq.heappop(lexico))
                
            return current
                        
                
            
                      
        