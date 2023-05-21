class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, parser: str) -> str:
        
        rep = defaultdict(str)
        
        for alpha in range(97,123):
            rep[chr(alpha)] = chr(alpha)
        
        def union(first, second):
            rep1, rep2 = find(first), find(second)
            
            if rep1 <= rep2:
                rep[rep2] = rep1
            else:
                rep[rep1] = rep2
        
        def find(letter):
            if rep[letter] == letter:
                return letter
            parent = find(rep[letter])
            rep[letter] = parent
            return parent
        
        for index in range(len(s1)):
            union(s1[index], s2[index])
        
        output = ""
       
        for index in range(len(parser)):
            if rep[find(parser[index])] and  rep[find(parser[index])] <= parser[index]:
                output += rep[find(parser[index])]
            else:
                output += parser[index]
        return output
        