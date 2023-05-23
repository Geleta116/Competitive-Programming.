class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        rep = defaultdict(int)
        
        for index, account in enumerate(accounts):
            rep[index] = index
            for email in range(1, len(account)):
                if account[email] not in rep:
                    rep[account[email]] = (index)
            
        
        
        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            
            if par1 <= par2:
                rep[par2] = par1
            else:
                rep[par1] = par2
                

        def find(node):
            if rep[node] == node:
                return node
            parent = find(rep[node])
            rep[node] = parent
            return parent
        
        
        
        for account in accounts:
            for index in range(2,len(account)):
                union(account[index - 1], account[index])
            
        reverse = defaultdict(list)
        
        for key in rep:
            find(key)
            
        for email in rep:
            if type(email) != int:
                reverse[rep[email]].append(email)
        
        
        for parent in reverse:
            reverse[parent].sort()
            
            
        answer = []
        
        for key in reverse:
            merged = []
            merged.append(accounts[int(key)][0])
            for email in reverse[key]:
                merged.append(email)
            answer.append(merged)
            
        
        return answer
        