class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.validRequests = 0
        
        def backtrack(index, request):
            checker = defaultdict(int)
            validator = True
            
            
            for req in request:
                checker[req[0]] -= 1
                checker[req[1]] += 1
            
            for each in checker.values():
                if each != 0 :
                    validator = False
                    break
            if validator:
                
                self.validRequests = max(self.validRequests, len(request))
            if index >= len(requests):
                return
            request.append(requests[index])
            backtrack(index + 1, request)
            request.pop()
            backtrack(index + 1, request)
            
        backtrack(0, [])
        return self.validRequests
                
            
            
        