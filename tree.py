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