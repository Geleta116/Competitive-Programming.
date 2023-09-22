class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        rank = defaultdict(int)
        par = defaultdict(int)
        friends = defaultdict(list)
        output = []
        
        for friend in range(1000):
            par[friend] = friend
            rank[friend] = 1
            
        def find(x): 
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        def union(num1, num2):
            par1, par2 = find(num1), find(num2)

            if par1 != par2:
                if rank[par1] >= rank[par2]:
                    rank[par1] += rank[par2]
                    par[par2] = par1
                else:
                    rank[par2] += rank[par1]
                    par[par1] = par2

        for request in requests:
           
            par_request1 = find(request[0])
            par_request2 = find(request[1])
            if par_request1 == par_request2:
                output.append(True)
                continue
            else:
                curr = True
                for restriction in restrictions:
                    par_restriction1 = find(restriction[0])
                    par_restriction2 = find(restriction[1])
                    if (par_request1 == par_restriction1 and par_request2 == par_restriction2) or (par_request1 == par_restriction2 and  par_request2 == par_restriction1):
                        curr = False
                        break
                if not curr:
                    output.append(False)
                else:
                    output.append(True)
                    union(find(request[0]),find(request[1]))
        return output
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
        
       