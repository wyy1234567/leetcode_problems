# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. 
# Each time the sliding window moves right by one position. Return the max sliding window.

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def max_sliding_window(nums, k)
    arr = []
    ans = []
    nums.each_with_index do |num, index|
        while !arr.empty? && nums[arr.last] < num
            arr.pop
        end
        arr << index
        if arr.first == index - k
            arr.shift
        end
        if index >= k - 1
            ans << nums[arr[0]]
        end
    end
    ans
end

print max_sliding_window([1,3,-1,-3,5,3,6,7], 3)