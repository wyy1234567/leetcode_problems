class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    #find max depth of a tree
    def maxDepth(self, root):
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right)+1

    def diameterOfBinaryTree(self, root):
        self.ans = 0
        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            
            self.ans = max(self.ans, left + right)
            
            return max(left, right)+1
        height(root)
        return self.ans
        
    
