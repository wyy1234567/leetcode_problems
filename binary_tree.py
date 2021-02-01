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
    
    def invertTree(self, root):
        if not root:
            return None
        
        leftTree = root.left
        
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(leftTree)
        
        return root

    def hasPathSum(self, root, sum):
        if not root:
            return False
        
        sum -= root.val
        
        if not root.left and not root.right:
            return sum == 0
        
        left = self.hasPathSum(root.left, sum)
        right = self.hasPathSum(root.right, sum)
        
        return left or right


    def isSubtree(self, s, t):
        
        if not s:
            return False

        #tell if two trees are identical from the root
        def areSame(s, t):
            if not s and not t:
                return True
            
            if not s or not t or s.val != t.val:
                return False
            
            left = areSame(s.left, t.left)
            right = areSame(s.right, t.right)
            
            return left and right
            
        return areSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    
    def isSymmetric(self, root):
        if not root:
            return True
        
        def same(r, l):
            if not r and not l:
                return True 
            
            if not r or not l:
                return False 
            
            if r.val != l.val:
                return False 
            
            return same(r.left, l.right) and same(r.right, l.left)

        return same(root.left, root.right)
    
    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if left == 0 or right == 0:
            return left + right +1
        
        return min(left, right)+1
        
    
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0 
        
        queue = [root]
        res = 0
        
        while queue:
            curr = queue.pop(0)
            if curr.left:
                if not curr.left.left and not curr.left.right:  
                    res += curr.left.val 
                queue.append(curr.left) 
            if curr.right:
                queue.append(curr.right)
                
        return res
    

    #Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
    def rightSideView(self, root):
        if not root:
            return []
        
        queue, res = [root], []
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                curr = queue.pop(0)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
                    
                if i == size - 1:
                    res.append(curr.val)
        
        return res

    # Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
    def isCousins(self, root, x, y):
        if not root:
            return False
        lmap = {}
        queue = [root]
        
        while queue:
            size = len(queue)
            level = set()
            
            for _ in range(size):
                curr = queue.pop(0)
                level.add(curr.val)
                
                if curr.left: 
                    queue.append(curr.left)
                    lmap[curr.left.val] = curr.val
                if curr.right: 
                    queue.append(curr.right)
                    lmap[curr.right.val] = curr.val
                
            if x in level and y in level and lmap[x] != lmap[y]:
                return True
        
        return False