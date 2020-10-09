from collections import defaultdict, deque

def vertcalTraversal(root):
    nhash = collections.defaultdict(list)
    queue = collections.deque()

    queue.append((root, 0))

    while queue:
        node, index = queue.popleft()
        if node:
            nhash[index].append(node.val)
            queue.append((node.left, index - 1))
            queue.append((node.right, index + 1))

    return [nhash[key] for key in sorted(nhash)]