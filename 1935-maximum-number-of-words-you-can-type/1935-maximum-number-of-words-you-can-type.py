class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        out = 0
        br = set([i for i in brokenLetters])
        text = text.split()
        wr = [set([j for j in i]) for i in text]
       
        for item in wr:
            flag = True
            for char in br:
                if char in item:
                    flag = False
                    break
            if flag:
                out += 1
                
        return out
        