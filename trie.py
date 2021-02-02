#Trie is also called prefix-tree, is useful in searching words, auto-complete words, etc 
#implement a trie with basic functions: insert(), search(), startsWith()

class TrieNode:

    def __init__(self):
        self.children = [None] * 26 
        self.isLeaf = False 

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.isLeaf = True 


    def search(self, word):
        current = self.root

        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                return False 
            current = current.children[index]
        return current and current.isLeaf

    def startsWith(self, prefix):
        current = self.root

        for letter in prefix:
            index = ord(letter) - ord('a')

            if not current.children[index]:
                return False 
            
            current = current.children[index]
        return True


