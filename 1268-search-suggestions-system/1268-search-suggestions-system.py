class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if curr.children[ord(char) -  ord('a')]:
                curr =  curr.children[ord(char) -  ord('a')]
            else:
                newNode = TrieNode()
                curr.children[ord(char) -  ord('a')] = newNode
                curr = newNode
        curr.is_end = True
    
    def searchPre(self, word):
        self.curr =  self.root
        self.out = []
        
        for char in word:
            if self.curr.children[ord(char) -  ord('a')]:
                self.curr =  self.curr.children[ord(char) -  ord('a')]
            else:
                return self.out
            
        self.dfs(self.curr, word)
        return self.out
    
    def dfs(self,node, curr):
        if not node:
            return
        
        elif len(self.out) >= 3:
            return
        
        elif node.is_end:
            self.out.append(curr)
            
         
        for i, child in enumerate(node.children):
            if child and len(self.out) < 3:
              
                self.dfs(child, curr + chr(97 + i))
        return
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        output = []
        for product in products:
            trie.insert(product)
        
        
        for idx in range(len(searchWord)):
            if trie.searchPre(searchWord[:idx + 1]):
                output.append(trie.searchPre(searchWord[:idx + 1]))
            else:
                print("sdf")
                output.append([])
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        