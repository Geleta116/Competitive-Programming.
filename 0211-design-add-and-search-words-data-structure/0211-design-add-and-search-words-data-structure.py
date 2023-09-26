class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        self.curr = self.root
        for char in word:
            if self.curr.children[ord(char)- ord('a')]:
                self.curr = self.curr.children[ord(char)- ord('a')]
            else:
                newNode = TrieNode()
                self.curr.children[ord(char)- ord('a')] = newNode
                self.curr = newNode
        self.curr.is_end = True
        

    def search(self, word: str) -> bool:
        self.curr = self.root
        return self.find(word, self.curr)
    
    def find(self, word, curr):
        if not word:
            return curr.is_end

        first_char = word[0]

        if first_char != '.':
            child = curr.children[ord(first_char) - ord('a')]
            if child:
                return self.find(word[1:], child)
            else:
                return False
        else:
            for child in curr.children:
                if child and self.find(word[1:], child):
                    return True
            return False

     
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)









