
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

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

def unique_paths(m, n)
    return 0 if m == 0 && n == 0
    return 1 if m == 0 || n == 0

    arr = [0] * n
    matrix = []
    m.times do 
        matrix << arr
    end

    for i in 0...m do 
        for j in 0...n do 
            if i == 0 && j == 0
                matrix[i][j] *= 1
            elsif i == 0 && j != 0
                matrix[i][j] = matrix[i][j - 1]
            elsif j == 0
                matrix[i][j] = matrix[i - 1][j]
            else
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
            end
        end
    end

    matrix[m-1][n-1]
end