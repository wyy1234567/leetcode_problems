# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7], output: [[3],[9,20],[15,7]]

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
# @return {Integer[][]}

#use BFS and queue to travel a tree by level order
def level_order(root)
    return [] if !root
    queue = [root]
    ans = []
    while !queue.empty? do 
        level_num = queue.size
        level = []
        for i in 0...level_num do
            queue.push(queue.first.left) if queue.first.left
            queue.push(queue.first.right) if queue.first.right
            level << queue.shift.val
        end
        ans << level
    end
    ans
end