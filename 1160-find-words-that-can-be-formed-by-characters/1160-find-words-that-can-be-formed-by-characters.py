class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch = Counter(chars)
        store = 0
        for word in words:
            wr = Counter(word)
            c= 0
            for char in wr:
                if wr[char]>ch[char]:
                    c = 1
                    break
            if not(c):
                store +=len(word)
                
        return store