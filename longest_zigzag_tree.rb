# Given a binary tree root, a ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right then move to the right child of the current node otherwise move to the left child.
# Change the direction from right to left or right to left.
# Repeat the second and third step until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).


# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer}

#dfs
def longest_zig_zag(root)
    return -1 if !root
    @max = 0
    def dfs(root, step, is_right)
        return -1 if !root
        @max = [@max, step].max
        if is_right
            dfs(root.left, step + 1, false)
            dfs(root.right, 1, true)
        else
            dfs(root.right, step + 1, true)
            dfs(root.left, 1, false)
        end
    end
    dfs(root.right, 1, true)
    dfs(root.left, 1, false)
    @max
end