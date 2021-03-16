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
        self.next = None 

    def connect(self, root):
        if not root:
            return None 
        
        level_first = root 
        
        while level_first:
            curr = level_first
            while curr:
                if curr.left:
                    curr.left.next = curr.right
                if curr.right and curr.next:
                    curr.right.next = curr.next.left 
                curr = curr.next
            level_first = level_first.left 
        
        return root
    
    def distributeCoins(self, root):
        self.ans = 0 
        
        def balance(node):
            if not node:
                return 0
            left = balance(node.left)
            right = balance(node.right)
            self.ans += abs(left) + abs(right)
            return node.val - 1 + left + right
        
        balance(root)
        return self.ans

    def boundaryOfBinaryTree(self, root):
        # write your code here
        if not root:
            return []
        left = self.find_left(root.left)
        leaves = self.find_leaves(root)
        right = self.find_right(root.right)
        
        if left and leaves and left[-1] == leaves[0]:
            leaves = leaves[1:]
        if leaves and right and leaves[-1] == right[-1]:
            leaves = leaves[:-1]
        return [root.val] + left + leaves + list(reversed(right))


    def find_left(self, root):
        res = []
        while root is not None:
            res.append(root.val)
            if root.left:
                root = root.left 
            elif root.right:
                root = root.right 
            else:
                break 
        return res 
    
    def find_right(self, root):
        res = []
        while root is not None:
            res.append(root.val)
            if root.right:
                root = root.right 
            elif root.left:
                root = root.left 
            else:
                break 
        return res 


    def find_leaves(self, root):
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
        
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
    
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None 
        self.flatten(root.left)
        self.flatten(root.right)
        
        if root.left:
            right = root.right 
            root.right = root.left 
            root.left = None 
            last = root
            while last.right:
                last = last.right 
            last.right = right 
    
# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

#preorder: root -> left -> right
#           5 
#         /   \
#       2      6
#     /   \
#    1      3              => [5, 2, 1, 3, 6]

    def verifyPreorder(self, preorder):
        low = float('-inf')
        stack = []

        for p in preorder:
            if p < low:
                return False 
            while stack and p > stack[-1]:
                low = stack[-1]
                stack.pop()
            stack.append(p)
        
        return True

    # Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
    #head -> left_subtree -> root -> right_subtree -> left_subtree 

    def treeToDoublyList(self, root):
        if not root:
            return None 

        def dfs(root):
            if not root:
                return None, None 
            
            left_head, left_tail = dfs(root.left)
            right_head, right_tail = dfs(root.right)

            if left_tail:
                left_tail.right = root 
                root.left = left_tail 
            if right_head:
                root.right = right_head 
                right_head.left = root 
            
            head = left_head or root or right_head 
            tail = right_tail or root or left_tail 

            return head, tail

        head, tail = dfs(root)
        tail.right = head 
        head.left = tail 

        return head
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
    #       3
    #     /    \ 
    #    9     20
    #         /  \
    #        15   7
    # preorder(this->left->rght): [3,9,20,15,7]
    # inorder(left->this->right):[9,3,15,20,7]
    def build_tree_preorder(self, preorder, inorder):
        if not preorder and not inorder:
            return None 
        
        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        for i in range(len(inorder)):
            if inorder[i] == root_val:
                root.left = self.build_tree_preorder(preorder[1:i+1], inorder[:i])
                root.right = self.build_tree_preorder(preorder[i+1:], inorder[i+1:])
                break 
                
        return root
    
    #       3
    #     /    \ 
    #    9     20
    #         /  \
    #        15   7
    # postorder(left->rght->this): [9,15,7,20,3]
    # inorder(left->this->right):[9,3,15,20,7]
    def build_tree_postorder(self, inorder, postorder):
        map_inorder = {}
        for i, v in enumerate(inorder):
            map_inorder[v] = i 
        
        def recur(low, high):
            if low > high:
                return None 
            root = TreeNode(postorder.pop())
            index_root = map_inorder[root.val]
            root.right = recur(index_root+1, high)
            root.left = recur(low, index_root - 1)
            return root 
        
        return recur(0, len(inorder)-1)

# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.
    def path_sumII(self, root, targetSum):
        if not root:
            return []
        
        res = []
        
        def backtrack(root, target, path):

            if target == root.val and (not root.left) and (not root.right):
                path.append(root.val)
                res.append(path)
                return 
            else:
                if root.left:   
                    backtrack(root.left, target-root.val, path+[root.val])
                if root.right:
                    backtrack(root.right, target-root.val, path+[root.val])
        
        backtrack(root, targetSum, [])
        return res
    

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        if not root.left and not root.right:
            return root.val 
        
        paths = self.find_path(root)
        
        res = 0 
        
        for p in paths:
            num = 0
            for i in range(len(p)):
                num = num + p[i] * (10 ** i)
            res += num
        return res
        
    
    def find_path(self, root):
        if not root:
            return []
        
        if not root.left and not root.right:
            return [[root.val]]
        
        
        left = self.find_path(root.left)
        right = self.find_path(root.right) 
        
        res = []
        
        for l in left:
            l.append(root.val)
            res.append(l)
            
        for r in right:
            r.append(root.val)
            res.append(r)
            
        return res

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def sortedListToBST(self, head):
        if not head:
            return None 
        slow, fast = head, head 
        prev_slow = None 
        while fast and fast.next:
            prev_slow = slow
            fast = fast.next.next
            slow = slow.next
            
        root = TreeNode(slow.val)
        if prev_slow:
            prev_slow.next = None 
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(slow.next)
        return root
        

class Node:
    def __init__(self, val=0):
        self.left, self.right = None, None
        self.val = val 
