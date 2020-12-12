# from collections import defaultdict, deque

# def vertcalTraversal(root):
#     from collections import defaultdict, deque
#     nhash = collections.defaultdict(list)
#     queue = collections.deque()

#     queue.append((root, 0))

#     while queue:
#         node, index = queue.popleft()
#         if node:
#             nhash[index].append(node.val)
#             queue.append((node.left, index - 1))
#             queue.append((node.right, index + 1))

#     return [nhash[key] for key in sorted(nhash)]



#Binary Tree Maximum Path Sum II
def maxSum(root):
    if not root:
        return -1
    return max(maxSum(root.left) + root.val, maxSum(root.right)+ root.val, root.val) 


class Solution:
    def maxPathSum(self, root):
        self.maxSum = float('-inf')
        self.pathSumRoot(root)
        return self.maxSum
    
    
    def pathSumRoot(self, root):
        if not root:
            return 0
        
        leftSum = self.pathSumRoot(root.left)
        if leftSum < 0: 
            leftSum = 0
        
        rightSum = self.pathSumRoot(root.right)
        if rightSum < 0: 
            rightSum = 0
            
        self.maxSum = max(self.maxSum, leftSum + rightSum + root.val)
        
        return max(leftSum + root.val, rightSum + root.val)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 
    
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and not root.left and not root.right:
            root = None
            
        return root

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return ans

    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True 
        if not root:
            return True
        
        left = self.depth(root.left)
        right = self.depth(root.right)
        
        if not self.flag:
            return False
        
        if abs(left - right) <= 1:
            return True
        else:
            return False
    
    def depth(self, root):
        if not root:
            return 0
        
        left = self.depth(root.left)
        right = self.depth(root.right)
        
        if abs(left - right) > 1:
            self.flag = False
            
        depth = max(left, right) + 1
        return depth