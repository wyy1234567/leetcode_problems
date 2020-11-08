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

def my_sqrt(x)
    start = 0
    last = x
    while start + 1 < last do 
        mid = start + (last - start) / 2
        if mid * mid < x
            start = mid
        else
            last = mid
        end
    end
    return start if start * start == x
    return last if last * last == x
    return start
end