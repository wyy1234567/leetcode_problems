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

def two_sum(numbers, target)
    low = 0
    high = numbers.length - 1
    while low < high do 
        small = numbers[low]
        large = numbers[high]
        sum = small + large
        if sum == target
            return [low + 1, high + 1]
        elsif sum < target
            low += 1
        else
            high -= 1
        end 
    end
    return nil
end

def merge(nums1, m, nums2, n)
    left = m - 1
    right = n - 1
    merge_ind = m + n - 1
            
    while (left >= 0 || right >= 0) do
        if left < 0
            nums1[merge_ind] = nums2[right]
            merge_ind -= 1
            right -= 1
        elsif right < 0
            nums1[merge_ind] = nums1[left]
            merge_ind -= 1
            left -= 1
        elsif nums2[right] > nums1[left]
            nums1[merge_ind] = nums2[right]
            right -= 1
            merge_ind -= 1
        else
            nums1[merge_ind] = nums1[left]
            left -= 1
            merge_ind -= 1
        end 
    end
    nums1
end