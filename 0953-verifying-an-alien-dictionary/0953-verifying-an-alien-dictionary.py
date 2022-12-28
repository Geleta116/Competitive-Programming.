class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {}
        converter = []
        for ind , char in enumerate(order):
            index[char] = ind
        for each_word in words:
            convertable = []
            for each_char in each_word :
                convertable.append(index[each_char])
            converter.append(convertable)
        i = 0
        j = 1
      
        
        
        
        while j < len(converter):
            if converter[i]> converter[j]:
                return False
            i+=1
            j+=1
        return True

        
        