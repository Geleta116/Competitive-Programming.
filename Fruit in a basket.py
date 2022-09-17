class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        e=0
        num_tree = 0
        store = {}
        while e<len(fruits):
            store[fruits[e]]=e
            if len(store)>=3:
                mini = min(store.values())
                del store[fruits[mini]]
                l = mini+1
            num_tree = max(num_tree,e-l+1)
            e+=1
        return num_tree
         
