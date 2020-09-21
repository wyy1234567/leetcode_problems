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

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

def num_islands(grid)
    return 0 if !grid || grid.empty? || grid[0].size = 0
    n = grid.size
    m = grid[0].size
    ans = 0
    for i in 0...n do 
        for j in 0...m do 
            if grid[i][j] == '1'
                mark_island(grid, i, j, n, m)
                ans += 1
            end
        end
    end
    ans
end

def mark_island(grid, x, y, n, m)
    queue = [[x, y]]
    x_dir = [0, 1, -1, 0]
    y_dir = [1, 0, 0, -1]
    grid[x][y] = '0'
    while !queue.empty? do 
        curr = queue.shift
        curr_x = curr[0]
        curr_y = curr[1]
        for i in 0...4 do 
            adj_x = curr_x + x_dir[i]
            adj_y = curr_y + y_dir[i]

            if adj_x < 0 || adj_x >= n || adj_y < 0 || adj_y >= m 
                next
            end

            if grid[adj_x][adj_y] == '1'
                grid[adj_x][adj_y] = '0'
                queue << [adj_x, adj_y]
            end
        end
    end
end

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16

def island_perimeter(grid)
    return 0 if !grid || grid.empty? || grid[0].size = 0
    count = 0
    neighbors = 0
    n = grid.size
    m = grid[0].size
    for i in 0...n do 
        for j in 0...m do 
            if grid[i][j] == 1
                count += 1
            end

            if i + 1 < n && grid[i + 1][j] == 1
                neighbors += 1
            end

            if j + 1 < m && grid[i][j + 1] == 1
                neighbors += 1
            end
        end
    end
    count * 4 - neighbors * 2
end

# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# Example:
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

def right_side_view(root)
    return [] if !root
    queue = [root]
    ans = []
    while !queue.empty? do 
        size = queue.size
        for i in 0...size do 
            curr = queue.shift
            queue << curr.left if curr.left
            queue << curr.right if curr.right
            if i == size - 1
                ans << curr.val 
            end
        end
    end
    ans
end