class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maximum = 0
       
        case = []
        for word in words:
            current = 0
            for letter in word:
                current |= 1 << ord(letter) - 96
            case.append(current)
        output = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if case[i] & case[j] == 0:
                    output = max(output, len(words[i])*len(words[j]))
        return output
        
            
        
        
        