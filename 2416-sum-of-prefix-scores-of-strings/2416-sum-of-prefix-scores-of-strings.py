class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.count = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
        

    def insert(self, word: str) -> None:
        
        curr =  self.root

        for char in word:
            if curr.children[ord(char) - ord('a')]:
                curr.children[ord(char) - ord('a')].count += 1
            else:
                newNode = TrieNode()
                curr.children[ord(char) - ord('a')] = newNode
                newNode.count += 1
            curr = curr.children[ord(char) - ord('a')]
        curr.is_end =  True
        
        

    def search(self, word: str) -> bool:
        self.curr = self.root
        temp = 0
        for char in word:      
            if self.curr.children[ord(char)- ord('a')] != None:
                temp += self.curr.count
                self.curr =  self.curr.children[ord(char)- ord('a')]
            else:
                return 0
        temp += self.curr.count
        return temp

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        output = []
        for word in words:
                output.append(trie.search(word))
           
        return output
    
    