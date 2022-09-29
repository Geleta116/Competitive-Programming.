class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ct = Counter(tasks)
        if n== 0 :
            return len(tasks)
        else:
            d = dict(ct)
            sortd = sorted(d.values(), reverse = True)
            maxi = sortd[0]
            counter = 0
            for i in sortd:
                if i == maxi:
                    counter+=1
            return max(((maxi-1)*(n+1) + counter),len(tasks))
            
        
