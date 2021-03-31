class Node:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie(object):

    def __init__(self):
        self.root = Node()
        

    def insert(self, word):
        curnode = self.root
        for val in word:
            if val in curnode.children:
                curnode = curnode.children[val]
            else:
                curnode.children[val] = Node()
                curnode = curnode.children[val]
                
        curnode.end = True

    def search(self, word):
        curnode = self.root
        
        for val in word:
            if val not in curnode.children:
                return False
            curnode = curnode.children[val]
            
        if curnode.end:
            return True
        return False
        

    def startsWith(self, prefix):
        curnode = self.root
        
        for val in prefix:
            if val not in curnode.children:
                return False
            curnode = curnode.children[val]
            
        return True
