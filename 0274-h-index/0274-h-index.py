class Solution:
    def hIndex(self, citations: List[int]) -> int:
            citations.sort()
            h_ind = []
            n = len(citations)
            c = []
            #ct = Counter(citations)
            #d = list(ct.values())
            for j,k in enumerate(citations):
                        h_ind.append([j,k])

            for i in  h_ind:
                    if n-i[0]<=i[1]:
                        return n-i[0]
            return 0
        
            citations.sort()
            h_ind = []
            n = len(citations)
            c = []
            #ct = Counter(citations)
            #d = list(ct.values())
            if n>1:
                for j,k in enumerate(citations):
                        h_ind.append([j,k])

                for i in  h_ind:
                    if n-i[0]>=i[1]:
                        c.append(i[1])
                if len(c)>0:
                    return max(c)
                else:
                    return n
            elif n == 1:
                if citations[0]==0:
                    return 0
                else:
                    return 1
            else:
                return []



