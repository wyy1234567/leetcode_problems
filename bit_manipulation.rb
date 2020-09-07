# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:
# Input: [2,2,1]
# Output: 1

#use XOR operator: 0^0 = 0, 0^x = x
def single_number(nums)
    a = 0
    nums.each do |num|
        a ^= num
    end
    a
end