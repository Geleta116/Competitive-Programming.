class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.count = 0
        self.is_end =  False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.root.is_end =  True
        self.Longest = ""
    
    def insert(self, word):
        curr =  self.root
        for char in word:
            if curr.children[ord(char) - ord('a')]:
                curr.children[ord(char) - ord('a')].count += 1
            else:
                newNode = TrieNode()
                curr.children[ord(char) - ord('a')] = newNode
                newNode.count = 1
            curr = curr.children[ord(char) - ord('a')]
        curr.is_end =  True
    
    def findLongest(self, word, node):
        if len(word) == 0:
            return True
        
        if node.is_end and self.findLongest(word[1:], node.children[ord(word[0]) - ord('a')]):
            if len(word) > len(self.Longest):
                self.Longest =  word
            elif len(word) == len(self.Longest) and word < self.Longest:
                self.Longest =  word
            return True
        
        else:
            return False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie =  Trie()
        words.sort()
        for word in words:
            trie.insert(word)
        for word in words:
            trie.findLongest(word, trie.root)
        
        return trie.Longest
        
        