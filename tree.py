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


import collections
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

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        if not t1:
            return t2
        if not t2:
            return t1
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        
        t1.val += t2.val 
        
        return t1

    def sortedArrayToBST(self, nums):
        root = self.buildTree(nums, 0, len(nums) - 1)
        return root
        
    def buildTree(self, arr, start_i, end_i): 
        if start_i < end_i: 
            return None 
        mid = (start_i + end_i) // 2 
        root = TreeNode(arr[mid])
        root.left = self.buildTree(arr, start_i, mid-1)
        root.right = self.buildTree(arr, mid+1, end_i)
        print(root.val)
        return root

    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = float('inf')
        nodeList = self.inorderTraversal(root) 
        
        for i in range(1, len(nodeList)): 
            diff = nodeList[i] - nodeList[i - 1]
            ans = min(diff, ans)
        return ans
        
        
    def inorderTraversal(self, root):
        if not root:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def zigzagLevelOrder(self, root):
        result = []
        if not root:
            return result 
        
        flag = 1
        queue = [root]
        
        while queue: 
            size = len(queue)
            level = []
            
            for _ in range(size):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result += [level[::flag]]
            flag *= -1
        return result 
    
    def distanceK(self, root: TreeNode, target: TreeNode, K: int):

        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))

        return []
    
    def averageOfLevels(self, root):
        result = []
        if not root:
            return result 
        
        queue = [root]
        
        while queue:
            size = len(queue)
            curr = 0 
            
            for _ in range(size):
                node = queue.pop(0)
                curr += node.val 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(curr/size)
        return result
    
    def findBottomLeftValue(self, root):
        if not root:
            return None
        levels = []
        queue = [root]
        
        while queue:
            size = len(queue)
            level = []
            
            for _ in range(size):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            levels.append(level)
        
        return levels[-1][0]
        