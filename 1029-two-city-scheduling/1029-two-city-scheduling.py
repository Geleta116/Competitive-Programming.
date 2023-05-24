class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = defaultdict(int)
        
        for index, cost in enumerate(costs):
            diff[(cost[0] - cost[1], index)] = cost
        
        sorted_diff = [diff[key] for key in  sorted(diff.keys())]
        print(sorted_diff)
        total = 0
        for i in range(len(costs)//2):
            total+= sorted_diff[i][0]
        for i in range(len(costs)//2 , len(costs)):
            total += sorted_diff[i][1]
        return total
    