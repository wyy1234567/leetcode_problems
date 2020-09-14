# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14

def check_perfect_number(num)
    return false if num == 1
    divisors = [1]
    for i in 2..Math.sqrt(num.abs) do 
        if num % i == 0
            divisors << i
            divisors << num / i
        end
    end
    print divisors
    divisors.sum == num
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