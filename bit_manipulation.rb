# x ^ 0s = x      x & 0s = 0      x | 0s = x
# x ^ 1s = ~x     x & 1s = x      x | 1s = 1s
# x ^ x = 0       x & x = x       x | x = x

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

# Given an integer n, return the number of trailing zeroes in n!.

# Example 1:
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

# Example 2:
# Input: 5
# Output: 1
# Explanation: 5! = 120, 1 trailing zero.

def trailing_zeroes(n)
    if n == 0
        return 0
    else
        return (n / 5 + trailing_zeroes(n / 5))
    end
end