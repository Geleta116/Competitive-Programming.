class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dict_i = defaultdict(list)
        for i,item in enumerate(nums):
            dict_i[item] = [item, i]
        for item in range(len(operations)):
            indi = dict_i[operations[item][0]][1]
            del dict_i[operations[item][0]]
            dict_i[operations[item][1]] = [operations[item][1],indi]
        output = []
        for item in dict_i:
            output.append(dict_i[item])
        
        output.sort(key = lambda x : x[1])
        
        res = [i[0] for i in output]
        return res
            