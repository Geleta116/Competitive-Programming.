class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.count = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.inserted =  defaultdict(int)
        

    def insert(self, word: str, val: int) -> None:
        
        curr =  self.root
        if word not in self.inserted:
            for char in word:
                if curr.children[ord(char) - ord('a')]:
                    curr.children[ord(char) - ord('a')].count += val
                else:
                    newNode = TrieNode()
                    curr.children[ord(char) - ord('a')] = newNode
                    newNode.count += val
                curr = curr.children[ord(char) - ord('a')]
            curr.is_end =  True
            self.inserted[word] = val
        else:
            for char in word:
                if curr.children[ord(char) - ord('a')]:
                    curr.children[ord(char) - ord('a')].count += (val - self.inserted[word])
                else:
                    newNode = TrieNode()
                    curr.children[ord(char) - ord('a')] = newNode
                    newNode.count += (val - self.inserted[word])
                curr = curr.children[ord(char) - ord('a')]
            curr.is_end =  True
            self.inserted[word] = val
            

    def sum(self, word: str) -> int:
        
        self.curr = self.root
        for char in word:      
            if self.curr.children[ord(char)- ord('a')] != None:
                self.curr = self.curr.children[ord(char)- ord('a')]
            else:
                return 0
        return self.curr.count
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)