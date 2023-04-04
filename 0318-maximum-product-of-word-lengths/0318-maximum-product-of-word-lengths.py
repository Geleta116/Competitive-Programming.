class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maximum = 0
        alphabet = {"a":1,"b":2,"c":4, "d":8, "e":16, "f": 2**5, "g":2**6, "h":2**7,"i":2**8,"j":2**9,"k":2**10,"l":2**11,"m":2**12, "n":2**13,"o":2**14, "p":2**15,"q":2**16,"r":2**17,"s":2**18,"t":2**19,"u":2**20,"v":2**21,"w":2**22,"x":2**23,"y":2**24,"z":2**25}
        
        case = []
        for word in words:
            current = 0
            for letter in word:
                current |= alphabet[letter]
            case.append(current)
        output = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if case[i] & case[j] == 0:
                    output = max(output, len(words[i])*len(words[j]))
        return output
        
            
        
        
        