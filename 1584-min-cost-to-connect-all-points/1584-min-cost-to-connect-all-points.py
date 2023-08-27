class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        distance = defaultdict(int)
        
        for i in range(len(points)):
            for j in range(i+ 1, len(points)):
                num = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distance[(tuple(points[i]), tuple(points[j]))] = num
            
        sorted_dict = dict(sorted(distance.items(), key=lambda item: item[1]))
        
        count = len(points)
        visited = set()
        cost = 0
        connections = defaultdict(set)
        par = defaultdict(tuple)
        rank = defaultdict(int)
        
        for item in points:
            rank[tuple(item)] = 1
            par[tuple(item)] = tuple(item)
            
        def find(row, col):
            
            if par[(row, col)] == (row, col):
                return (row, col)
            
            r, c = par[(row,col)]
            par[(row, col)] = find(r, c)
            return par[(row, col)]
        
        
            
        
        for key in sorted_dict:
            
            point1, point2 = key
            x1,y1 = point1
            x2,y2 = point2
            
            par1, par2 = find(x1,y1), find(x2,y2)
            
            if par1 == par2:
                continue
            else:
                if rank[par1] >= rank[par2]:
                    cost += sorted_dict[key]
                    rank[par1] += rank[par2]
                    par[par2] = par1
                    find(x2,y2)
                else:
                    cost += sorted_dict[key]
                    rank[par2] += rank[par1]
                    par[par1] = par2
                    find(x1,y1)

            
        return cost