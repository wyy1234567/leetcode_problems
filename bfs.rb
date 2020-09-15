# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3

def maxDepth(root)
    return 0 if !root
    queue = [root]
    height = 0
    while !queue.empty? do
        size = queue.size
        size.times do 
            curr = queue.shift
            curr.children.each do |c|
                queue << c
            end
        end
        height += 1
    end
    height
end