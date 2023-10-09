class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        temp = []
        for idx in range(len(gas)):
            temp.append(gas[idx] - cost[idx])
        
        if sum(temp) < 0:
            return -1
        
        sectemp = temp + temp
        idx = 0
        while idx < len(temp):
            if sectemp[idx] < 0:
                idx += 1
                continue
                
            running = 0
            for item in range(idx, idx + len(temp)):
                running += sectemp[item]
                if running < 0:
                    idx = item + 1
                    break
            if running >= 0:
                return idx
        return -1
                
        
        
        