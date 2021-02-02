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


def findWords(board, words):
    trie = Trie()

    for w in words:
        trie.insert(w)
    
    node = trie.root 
    res = []
    
    def helper(board, i, j, path, node, res):

        if node.isLeaf:
            res.append(path)
            node.isLeaf = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        tmp = board[i][j]
        node = node.children[ord(tmp) - ord('a')]
        if not node:
            return 
        board[i][j] = "#"
        helper(board, node, i+1, j, path+tmp, res)
        helper(board, node, i-1, j, path+tmp, res)
        helper(board, node, i, j-1, path+tmp, res)
        helper(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            helper(board, i, j, "", node, res)

    return res
