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

def max_envelopes(envelopes)
    return 0 if !envelopes
    return 1 if envelopes.size == 1
    envelopes = envelopes.sort
    arr = [0] * envelopes.size
    max = 0
    for i in 0...envelopes.size do 
        arr[i] = 1
        for j in 0...i do 
            if envelopes[j][0] < envelopes[i][0] && envelopes[j][1] < envelopes[i][1]
                arr[i] = arr[i] > arr[j] + 1 ? arr[i] : arr[j] + 1
            end
        end
        max = [max, arr[i]].max
    end
    max
end

def find_complement(num)
    mask = ~0
    while (num & mask) do 
        mask <<= 1
    end
    ~mask & ~num
end

def to_hex(num)
    map = {0 => '0',1 => '1',2 => '2',3 => '3',4 => '4',5 => '5',6 => '6',7 => '7',8 => '8',9 => '9',10 => 'a',11 => 'b',12 => 'c',13 => 'd',14 => 'e',15 => 'f'}
    return '0' if num == 0
    result = ''
    while num != 0 && result.size < 8 do 
        result = map[(num & 15)] + result
        num = num >> 4
    end
    result
end

def num_sub(s)
    return 0 if !s
    curr = 0
    ans = 0
    for i in 0...s.size do 
        if s[i] == '1'
            curr += 1
            ans += curr
        else
            curr = 0
        end
    end
    ans % (10 ** 9 + 7)
end

def self_dividing_numbers(left, right)
    ans = []
    for i in left..right do 
        if is_self_divided(i)
            ans << i
        end
    end
    ans
end

def is_self_divided(num)
    n = num
    while n > 0 do 
        curr = n % 10
        if curr == 0 || num % curr != 0
            return false
        end
        n /= 10
    end
    return true
end

def license_key_formatting(s, k)
    string = ''
    index = s.size - 1
    while index >= 0 do 
        if s[index] != '-'
            string = string + ((string.size % (k + 1) == k) ? '-' : '')
            string += s[index]
        end
        index -= 1
    end
    string.upcase.reverse
end


def is_power_of_four(num)
    s = num.to_s(2)
    zero_count = s[1..s.size - 1].count('0')
    if s[0] == '1' && zero_count == s.size - 1 && zero_count % 2 == 0
        return true
    end
    return false
end

def is_match(s, p)
    return false if !s || !p
    column = [false] * (p.size + 1)
    dp = []
    (s.size + 1).times do 
        dp << Array.new(column)
    end
    
    dp[0][0] = true
    for i in 1..p.size do 
        if p[i - 1] == '*' 
            dp[0][i] = dp[0][i-2]
        end
    end
    
    for i in 1..s.size do 
        for j in 1..p.size do 
            if p[j-1] == s[i-1] || p[j-1] == '.'
                dp[i][j] = dp[i-1][j-1]
            elsif p[j - 1] == '*'
                if p[j - 2] == s[i - 1] || p[j - 2] == '.'
                    dp[i][j] = dp[i-1][j] || dp[i][j - 2]
                else
                    dp[i][j] = dp[i][j - 2]
                end
            end
        end
    end
    print dp
    dp[s.size][p.size]
end

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