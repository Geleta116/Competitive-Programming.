class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root =  TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if curr.children[ord(char) - ord('a')]:
                curr = curr.children[ord(char) - ord('a')]
            else:
                newNode = TrieNode()
                curr.children[ord(char) - ord('a')] = newNode
                curr =  newNode
        curr.is_end = True
    
    def search(self, word):
        curr = self.root
        for char in word:
            if curr.children[ord(char) - ord('a')]:
                curr = curr.children[ord(char) - ord('a')]
            else:
                return False
        return curr.is_end
       

    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        @cache
        def dfs(word):
            if not word:
                return True
            for idx, char in enumerate(word):
                if trie.search(word[:idx + 1]):
                    store = dfs(word[idx + 1 :])
                    if store:
                        return True
            return False     
            
        return dfs(s) 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        