# 基本原理

# 0s 表示一串 0，1s 表示一串 1。

# x ^ 0s = x      x & 0s = 0      x | 0s = x
# x ^ 1s = ~x     x & 1s = x      x | 1s = 1s
# x ^ x = 0       x & x = x       x | x = x
# 利用 x ^ 1s = ~x 的特点，可以将一个数的位级表示翻转；利用 x ^ x = 0 的特点，可以将三个数中重复的两个数去除，只留下另一个数。

# 1^1^2 = 2
# 利用 x & 0s = 0 和 x & 1s = x 的特点，可以实现掩码操作。一个数 num 与 mask：00111100 进行位与操作，只保留 num 中与 mask 的 1 部分相对应的位。

# 01011011 &
# 00111100
# --------
# 00011000
# 利用 x | 0s = x 和 x | 1s = 1s 的特点，可以实现设值操作。一个数 num 与 mask：00111100 进行位或操作，将 num 中与 mask 的 1 部分相对应的位都设置为 1。

# 01011011 |
# 00111100
# --------
# 01111111
# 位与运算技巧

# n&(n-1) 去除 n 的位级表示中最低的那一位 1。例如对于二进制表示 01011011，减去 1 得到 01011010，这两个数相与得到 01011010。

# 01011011 &
# 01011010
# --------
# 01011010
# n&(-n) 得到 n 的位级表示中最低的那一位 1。-n 得到 n 的反码加 1，也就是 -n=~n+1。例如对于二进制表示 10110100，-n 得到 01001100，相与得到 00000100。

# 10110100 &
# 01001100
# --------
# 00000100
# n-(n&(-n)) 则可以去除 n 的位级表示中最低的那一位 1，和 n&(n-1) 效果一样。

# 移位运算

# >> n 为算术右移，相当于除以 2n，例如 -7 >> 2 = -2。

# 11111111111111111111111111111001  >> 2
# --------
# 11111111111111111111111111111110
# >>> n 为无符号右移，左边会补上 0。例如 -7 >>> 2 = 1073741822。

# 11111111111111111111111111111001  >>> 2
# --------
# 00111111111111111111111111111111
# << n 为算术左移，相当于乘以 2n。-7 << 2 = -28。

# 11111111111111111111111111111001  << 2
# --------
# 11111111111111111111111111100100
# mask 计算

# 要获取 111111111，将 0 取反即可，~0。

# 要得到只有第 i 位为 1 的 mask，将 1 向左移动 i-1 位即可，1<<(i-1) 。例如 1<<4 得到只有第 5 位为 1 的 mask ：00010000。

# 要得到 1 到 i 位为 1 的 mask，(1<<i)-1 即可，例如将 (1<<4)-1 = 00010000-1 = 00001111。

# 要得到 1 到 i 位为 0 的 mask，只需将 1 到 i 位为 1 的 mask 取反，即 ~((1<<i)-1)。

# Java 中的位操作

# static int Integer.bitCount();           // 统计 1 的数量
# static int Integer.highestOneBit();      // 获得最高位
# static String toBinaryString(int i);     // 转换为二进制表示的字符串

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

# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:
# Input: 16
# Output: true

# Example 2:
# Input: 5
# Output: false
# Follow up: Could you solve it without loops/recursion?

def is_power_of_four(num)
    s = num.to_s(2)
    zero_count = s[1..s.size - 1].count('0')
    if s[0] == '1' && zero_count == s.size - 1 && zero_count % 2 == 0
        return true
    end
    return false
end


# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:
# Input: [3,0,1]
# Output: 2

def missing_number(nums)
    missing = nums.size
    nums.each_with_index do |num, index|
        missing ^= index ^ num
    end
    missing
end