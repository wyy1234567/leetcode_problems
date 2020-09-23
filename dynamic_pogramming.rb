
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]

#find min path from bottom to top
def minimum_total(triangle)
    return 0 if !triangle || triangle.empty? || triangle[0].empty?
    return triangle[0][0] if triangle.size < 2

    i = triangle.size - 2
    while i >= 0 do 
        for j in 0...triangle[i].size do 
            triangle[i][j] += [triangle[i + 1][j], triangle[i + 1][j + 1]].min
        end
    end

    triangle[0][0]
end

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
# Example:
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum

def min_path_sum(grid)
    return 0 if !grid || !grid[0]
    return grid[0].last if grid.size < 1

    for i in 0...grid.size do 
        for j in 0...grid[i].size do 
            if i == 0 && j == 0
                grid[i][j] *= 1
            elsif i == 0 && j != 0
                grid[i][j] += grid[i][j - 1]
            elsif j == 0 
                grid[i][j] += grid[i - 1][j]
            else
                grid[i][j] += [grid[i][j - 1], grid[i - 1][j]].min
            end
        end
    end
    grid.last.last
end