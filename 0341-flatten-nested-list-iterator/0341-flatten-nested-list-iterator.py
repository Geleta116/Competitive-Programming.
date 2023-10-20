# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nested = nestedList
        self.res = []
        for items in nestedList:
            if items.isInteger():
                self.res.append(items.getInteger())
                continue
            store = self.iterator(items)
            if store:
                self.res.extend(store)
        
        if self.res == [] and nestedList[0].getInteger():
            self.res= [nestedList[0].getInteger()]
        self.idx = 0   
    
    def next(self) -> int:
        store = self.res[self.idx]
        self.idx += 1
        return store
    
    def hasNext(self) -> bool:
        if self.idx < len(self.res):
            return True
        return False
    
    def iterator(self, nestedInt):
        curr = nestedInt.getList()
        out = []
        for item in curr:
            if item.isInteger():
                out.append(item.getInteger())
            else:
                store = self.iterator(item)
                if store:
                    out.extend(store)
        return out
                
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())