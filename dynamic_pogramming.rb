
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

# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 1:
#     Input: 2
#     Output: 2
#     Explanation: There are two ways to climb to the top.
#     1. 1 step + 1 step
#     2. 2 steps

def climb_stairs(n)
    return 0 if n == 0
    return 1 if n == 1
    arr = [0, 1]
    for i in 2..n + 1 do 
        arr << arr[i - 1] + arr[i - 2]
    end
    arr.last
end

# Given an unsorted array of integers, find the length of longest increasing subsequence.
# Example:
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

def length_of_lis(nums)
    return 0 if !nums
    return 1 if nums.size == 1
    arr = [0] * nums.size
    max = 0
    for i in 0...nums.size do 
        arr[i] = 1
        for j in 0...i do 
            if nums[j] < nums[i]
                arr[i] = arr[i] > arr[j] + 1 ? arr[i] : arr[j] + 1 
            end
        end
        max = [max, arr[i]].max
    end
    max
end

# You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
# What is the maximum number of envelopes can you Russian doll? (put one inside other)
# Note:
# Rotation is not allowed.
# Example:
# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3 
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

def max_envelopes(envelopes)
    return 0 if !envelopes
    return 1 if envelopes.size == 1
    envelopes = envelopes.sort
    max = 0
    dp = [0] * envelopes.size
    for i in 0...envelopes.size do 
        dp[i] = 1
        for j in 0...i do 
            if envelopes[i][0] > envelopes[j][0] && envelopes[i][1] > envelopes[j][1]
                dp[i] = dp[i] > dp[j] + 1 ? dp[i] : dp[j] + 1
            end
        end
        max = [max, dp[i]].max
    end
    max
end

# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
# Si % Sj = 0 or Sj % Si = 0.
# If there are multiple solutions, return any subset is fine.
# Example 1:
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# Example 2:
# Input: [1,2,4,8]
# Output: [1,2,4,8]

def largest_divisible_subset(nums)
    return [] if !nums
    return nums if nums.size == 1
    nums = nums.sort
    dp = [0] * nums.size #record the max size before curr index
    pre = [0] * nums.size #record pre index of curr index
    size = 0
    index = -1
    ans = []
    for i in 0...nums.size do 
        pre[i] = -1
        dp[i] = 1
        
        for j in 0...i do 
            if nums[i] % nums[j] == 0 && dp[i] < 1 + dp[j]
                dp[i] = dp[j] + 1
                pre[i] = j
            end
        end
        
        if size <= dp[i]
            size = dp[i]
            index = i
        end
    end
    
    for i in 0...size do 
        ans.unshift(nums[index]) 
        index = pre[index]
    end
    ans
end


# 91. Decode Ways
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
# Example 1:
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
def num_decodings(s)
    return 0 if !s || s == '0'
    return 1 if s.size == 1
    dp = [0] * (s.size + 1)
    dp[0] = 1
    dp[1] = s[0] == '0' ? 0 : 1

    for i in 2..s.size do 
        char = s[i - 1].to_i
        chars = s[(i - 2)..(i - 1)].to_i

        if char >= 1 && char <= 9
            dp[i] += dp[i - 1]
        end

        if chars >= 10 && chars <= 26
            dp[i] += dp[i - 2]
        end
    end

    dp.last
end
