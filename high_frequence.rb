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
