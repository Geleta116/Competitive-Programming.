class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(27)]
        self.is_end =  False
        self.weight = 0
        

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for i, eachWord in enumerate(words):  
            for idx in range(len(eachWord)):
                word = eachWord[idx:] + "{" + eachWord
                self.insert(word, i)
                
    def insert(self, word: str, index) -> None:
        self.curr = self.root
        for char in word:
            self.curr.weight = index
            if self.curr.children[ord(char) - ord('a')]:
                self.curr = self.curr.children[ord(char) - ord('a')]
            else:
                newNode = TrieNode()
                newNode.weight = index
                self.curr.children[ord(char) - ord('a')] = newNode 
                self.curr = newNode
        self.curr.weight = index
        self.curr.is_end = True
   
    def startsWith(self, prefix: str) -> bool:
        
        self.curr = self.root
        for char in prefix:
            if self.curr.children[ord(char)- ord('a')]:
                self.curr = self.curr.children[ord(char)- ord('a')]
            else:
                return -1
        return self.curr.weight
    
    def f(self, pref: str, suff: str) -> int:
        return self.startsWith(suff+ "{" + pref)
        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)