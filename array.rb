# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

#use two pointers start from the edge to center
def max_area(height)
    left = 0
    right = height.size - 1
    max_area = 0
    while left < right do 
        max_area = [max_area, ([height[left], height[right]].min) * (right - left)].max
        if height[left] < height[right]
            left += 1
        else
            right -= 1
        end
    end
    max_area
end

# puts max_area([1,8,6,2,5,4,8,3,7])

def remove_duplicates(nums)
    return 0 if nums.empty?
    return 1 if nums.size == 1
    fast = 1
    slow = 0
    count = 1
    while (fast < nums.size) do 
        if nums[slow] == nums[fast]
            fast += 1
        else
            slow += 1
            nums[slow] = nums[fast]
            count += 1
        end
    end
    # nums[0..slow]
    nums[0, count]
end

print remove_duplicates([0,0,1,1,1,2,2,3,3,4])


# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example 1:
# Given nums = [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length.
def remove_element(nums, val)
    return 0 if nums.empty? || (nums.size == 1 && nums[0] == val)
    start = 0
    nums.each_with_index do |num, index|
        if num != val
            nums[start] = num
            start += 1
        end
    end
    nums[0..(start - 1)]
end

print remove_element([3,2,2,3], 3)
print remove_element([3,2,2,2,3,2,3], 3)


# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def max_sub_array(nums)
    return 0 if nums.empty?
    return nums[0] if nums.size == 1
    dp = [0] * nums.size
    dp[0] = nums[0]
    max = dp[0]
    
    for i in 1...nums.size do
        dp[i] = nums[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0)
        max = [max, dp[i]].max
    end
    max
end


# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

def plus_one(digits)
    num = 0
    digits.each_with_index do |digit, index|
        num = num * 10 + digit
    end
    num += 1
    ans = []
    while num > 0 do 
        ans.unshift(num % 10)
        num = num / 10
    end
    ans
end

# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# Example:
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

def generate(num_rows)
    ans = [[1], [1, 1]]
    return [] if num_rows == 0
    return [[1]] if num_rows == 1
    return ans if num_rows == 2
    
    for i in 3..num_rows do 
        curr_arr = [1] * i
        for j in 1..i - 2 do
            curr_arr[j] = ans[i - 2][j - 1] + ans[i - 2][j]
        end
        ans << curr_arr
    end
    ans
end


# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.


def max_profit(prices)
    min_price = prices[0]
    max_pro = 0 
    price.each do |price|
        if price <= min_price
            min_price = price
        elsif price - min_price > max_pro
            max_pro = price - min_price
        end
    end
    max_pro
end

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:
# Input: [3,2,3]
# Output: 3

#Boyer-Moore Voting Algorithm
def majority_element(nums)
    count = 0 
    ans = 0
    nums.each do |num|
        if count == 0
            ans = num
        end
        count += ans == num ? 1 : -1
    end
    ans
end


# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [5,6]

def find_disappeared_numbers(nums)
    ans = []
    for i in 0...nums.size do 
        index = nums[i].abs - 1
        if nums[index] > 0 
            nums[index] = -1 * nums[index]
        end
    end
    
    for i in 0...nums.size do 
        if nums[i] > 0
            ans << i + 1
        end
    end
    ans
end


# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
# Example:
# Input:
# [1,2,3]
# Output:
# 3
# Explanation:
# Only three moves are needed (remember each move increments two elements):
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

def min_moves(nums)
    nums.sum - nums.size * nums.min
end

# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
# Example 1:
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.

def repeated_substring_pattern(s)
    return false if !s
    (s + s)[1...-1].include?(s)
end

# Given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

def find_radius(houses, heaters)
    houses = houses.sort
    heaters = heaters.sort
    res = 0
    i = 0
    houses.each do |h|
        while i < heaters.size - 1 && heaters[i] + heaters[i + 1] <= h * 2 do 
            i += 1
        end
        res = [res, (heaters[i] - h).abs].max 
    end
    res
end

# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
def next_greater_element(nums1, nums2)
    hash = {}
    stack = []
    nums2.each do |num|
        while !stack.empty? && num > stack.last do 
            hash[stack.pop] = num
        end
        stack << num
    end
    
    ans = []
    nums1.each do |num|
        if hash[num]
            ans << hash[num]
        else
            ans << -1
        end
    end
    ans
end

# # Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

def find_relative_ranks(nums)
    hash = {}
    nums.each_with_index do |num, index|
        hash[num] = index
    end
    hash = hash.sort.to_h
    print hash
    count = 0
    hash.each do |k, v|
        if count == nums.size - 3
            nums[v] = "Bronze Medal"
        elsif count == nums.size - 2
            nums[v] = "Silver Medal"
        elsif count == nums.size - 1
            nums[v] = "Gold Medal"
        else
            nums[v] = (nums.size - count).to_s
        end
        count += 1
    end
    nums
end

# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.

def find_pairs(nums, k)
    return 0 if k < 0
    hash = {}
    count = 0
    nums.each do |num|
        if hash[num]
            if k == 0 && hash[num] == 1
                count += 1
            end
            hash[num] += 1
        else
            if hash[num - k]
                count += 1
            end
            if hash[num + k]
                count += 1
            end
            hash[num] = 1
        end
    end
    count
end

# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True

def can_place_flowers(flowerbed, n)
    i = 0
    while i < flowerbed.size do 
        if (flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.size - 1 || flowerbed[i + 1] == 0))
            flowerbed[i] = 1
            n -= 1
        end
        
        i += 1
    end
    
    n <= 0
end

# Given an array of integers nums, write a method that returns the "pivot" index of this array.
# We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.
# Input: nums = [1,7,3,6,5,6]
# Output: 3

def pivot_index(nums)
    sum = nums.sum
    left_sum = 0
    nums.each_with_index do |num, i|
        if left_sum == sum - left_sum - num
            return i
        end
        left_sum += num
    end
    return -1
end