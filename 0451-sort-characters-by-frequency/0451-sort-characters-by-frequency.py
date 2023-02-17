class Solution:
    def frequencySort(self, s: str) -> str:
        ct = Counter(s)
        ls = []
        for item in ct:
            temp = []
            temp.append(ct[item])
            temp.append(item)
            ls.append(temp)
        ls.sort(reverse=True)
        strr= ""
        for i in ls:
            strr += i[1]*i[0]
        
        return strr
        
        
        