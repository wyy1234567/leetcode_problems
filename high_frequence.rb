# 78. Subsets
# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
# Input: nums = [1,2,3]
# Output:[[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]

def subsets(nums)
    return nil if !nums
    return [[]] if nums.size == 0
    ans = []
    subset = []
    helper(nums, subset, ans, 0)
    ans
end

def helper(nums, subset, ans, start_index)
    ans << Array.new(subset)
    for i in start_index...nums.size do 
        subset << nums[i]
        helper(nums, subset, ans, i + 1)
        subset.pop
    end
end

# 90. Subsets II
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
# Input: [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

def subsets_with_dup(nums)
    return nil if !nums
    return [[]] if nums.size == 0
    ans = []
    subset = []
    nums = nums.sort
    dup_helper(nums, subset, ans, 0)
    ans
end

def dup_helper(nums, subset, ans, start_index)
    ans << Array.new(subset)
    for i in start_index...nums.size do 
        if i != start_index && nums[i] == nums[i - 1]
            next
        end
        subset << nums[i]
        dup_helper(nums, subset, ans, i + 1)
        subset.pop
    end
end

# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

def is_match(s, ps)
    return false if !s || !ps
    column = [false] * (ps.size + 1)
    dp = []
    (s.size + 1).times do 
        dp << Array.new(column)
    end

    dp[0][0] = true

    for i in 1..ps.size do 
        if ps[i - 1] == '*'
            dp[0][i] = dp[0][i-2]
        end
    end

    for i in 1..s.size do 
        for j in 1..p.size do 
            if s[i-1] == ps[j-1] || ps[j-1] == '.'
                dp[i][j] = dp[i-1][j-1]
            elsif ps[j-1] == '*'
                if ps[j-2] == s[i - 1] || ps[j-2] == '.'
                    dp[i][j] = dp[i - 1][j] || dp[i][j-2]
                else
                    dp[i][j] = dp[i][j-2]
                end
            end
        end
    end

    dp[s.size][ps.size]
end

# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).