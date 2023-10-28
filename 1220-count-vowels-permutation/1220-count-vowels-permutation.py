class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        graph = defaultdict(list)
        graph["a"] = ["e"]
        graph["e"] = ["a","i"]
        graph["i"] = ["a","e", "o", "u"]
        graph["o"] = ["i", "u"]
        graph["u"] = ["a"]
        
        @cache
        def dp(char, left):
            if left == 0:
                return 1
            out = 0
            for child in graph[char]:
                out += dp(child, left - 1)
            return out
        
        output = 0
        for char in graph.keys():
            output += dp(char, n - 1)
            
        return output % (10**9 + 7)
                