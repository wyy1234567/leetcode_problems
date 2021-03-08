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
    
    