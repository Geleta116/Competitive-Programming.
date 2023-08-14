from collections import defaultdict

class LockingTree:

    def __init__(self, parent):
        self.parent = parent
        self.children = defaultdict(list)
        self.locked = [False for _ in range(len(parent))]
        self.owner = [-1 for _ in range(len(parent))]
        for i in range(len(parent)):
            if parent[i] != -1:
                self.children[parent[i]].append(i)

    def lock(self, num, user):
        if self.locked[num]:
            return False
        self.locked[num] = True
        self.owner[num] = user
        return True

    def unlock(self, num, user):
        if not self.locked[num] or self.owner[num] != user:
            return False
        self.locked[num] = False
        self.owner[num] = -1
        return True

    def upgrade(self, num, user):
        if self.locked[num] or self.has_locked_ancestor(num, user):
            return False
        if self.has_locked_child(num):
            self.locked[num] = True
            self.owner[num] = user
            self.unlock_children(num)
            return True
        return False

    def has_locked_ancestor(self, num, user):
        curr = num
        while curr != -1:
            if self.locked[curr]:
                return True
            curr = self.parent[curr]
        return False
    
    def has_locked_child(self, num):
        if self.locked[num]:
            return True
        for child in self.children[num]:
            curr = self.has_locked_child(child)
            if curr:
                return True
        return False
    
    def unlock_children(self, num):
        for child in self.children[num]:
            self.locked[child] = False
            self.owner[child] = -1
            self.unlock_children(child)  # Recursively unlock descendants
