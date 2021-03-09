# https://leetcode.com/problems/powx-n/
def pow_recursion(x, n):
    if n == 0:
        return 1 
    
    if n < 0:
        return 1.0 / pow_recursion(x, -n)
    
    if n % 2 == 0:
        return pow_recursion(x, n // 2) * pow_recursion(x, n // 2)
    else:
        return pow_recursion(x, n // 2) * pow_recursion(x, n // 2) * x


def pow_iteration(x, n):
    if n == 0 or x == 1:
        return 1 
    if n == 1:
        return x 
    result = 1 

    if n < 0:
        return 1 / (x * pow_iteration(x, -(n+1)))
    
    while n > 1:
        if n % 2 == 1:
            result = result * n 
        
        x = x * x 
        n //= 2
    result *=  x 

    return result

def threeSum(nums):
        if len(nums) < 3:
            return []
        nums.sort()
        size = len(nums)
        result = []
        def two_sum(nums, target, left, right, result):
            last_pair = None 
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    if (nums[left], nums[right]) != last_pair:
                        result.append([-target, nums[left], nums[right]])
                    last_pair = (nums[left], nums[right])
                    right -= 1
                    left += 1
                elif curr_sum < target:
                    left += 1 
                else:
                    right -= 1
        
        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            two_sum(nums, -nums[i], i+1, size - 1, result)
        
        return result
    
    
# Given a list of non-negative integers nums, arrange them such that they form the largest number.
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
def largestNumber(nums):
    nums = merge_sort(nums, 0, len(nums)-1)
    res = ''
    for n in nums:
        res += str(n)
    
    return str(int(res))

def merge_sort(nums, left, right):
    if left > right:
        return 
    if left == right:
        return [nums[left]]
    
    mid = left + (right - left) // 2
    left_half = merge_sort(nums, left, mid)
    right_half = merge_sort(nums, mid + 1, right)

    return merge(left_half, right_half)

def compare(n1, n2):
    return str(n1) + str(n2) > str(n2) + str(n1)

def merge(l1, l2):
    res, i, j = [], 0, 0

    while i < len(l1) and j < len(l2):
        if compare(l1[i], l2[j]):
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1 
    
    res.extend(l1[i:] or l2[j:])
    return res

def findMaximumXOR(nums):
    res = 0
    mask = 0 
    for i in range(31,-1,-1):
        mask = mask | (1 << i)
        dic = set()
        
        for num in nums:
            dic.add(num & mask)    
        
        temp = res | (1 << i) 
        
        for prefix in dic:
            if temp ^ prefix in dic:
                res = temp
                break     
    return res
