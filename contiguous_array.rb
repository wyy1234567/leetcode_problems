# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

#prefix + hash map
def find_max_length(nums)
    return 0 if nums.empty?
    hash = {}
    sum = 0
    max = 0
    nums.each_with_index do |num, index|
        sum += num > 0 ? 1 : -1
        if sum == 0 
            max = [max, index + 1].max
        elsif hash[sum]
            max = [max, index - hash[sum]].max
        else
            hash[sum] = index
        end
    end
    max
end

puts find_max_length([0, 0, 1, 0, 0, 0, 1, 1])
puts find_max_length([0, 0])
puts find_max_length([0, 1])