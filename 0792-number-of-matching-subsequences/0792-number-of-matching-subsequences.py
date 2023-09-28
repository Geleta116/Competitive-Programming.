class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def search(self, word: str, s: str) -> bool:
        curr = self.root
        idx = 0
        givenIdx = 0  
        while idx < len(word) and givenIdx < len(s):
            char = word[idx]
            if curr.children[ord(char) - ord('a')] is not None:
                idx += 1
                curr = curr.children[ord(char) - ord('a')]
            else:
                if curr.is_end:
                    return False
                curr = curr.children[ord(s[givenIdx]) - ord('a')] 
            givenIdx += 1
        
        return idx == len(word) 

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if curr.children[ord(char) - ord('a')] is not None:
                curr = curr.children[ord(char) - ord('a')]
            else:
                new_node = TrieNode()
                curr.children[ord(char) - ord('a')] = new_node
                curr = new_node
        curr.is_end = True

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        trie.addWord(s)
        count = 0
        visited = defaultdict(int)
        for word in words:
            if word not in visited:
                if trie.search(word, s):
                    visited[word] = 1
                    count += 1
                else:
                    visited[word] = -1
            else:
                if visited[word] == 1:
                    count += 1
                else:
                    continue
        return count
