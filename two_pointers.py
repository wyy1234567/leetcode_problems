
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
def maxWater(height):
    size = len(height)
    left, right = 0, size - 1
    res = 0
        
    while left < right:
        area = (right - left) * min(height[left], height[right])
        res = max(res, area)
        if height[left] < height[right]:
            left += 1 
        else:
            right -= 1
    
    return res


# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
def productExceptSelf(nums):
    size = len(nums)
    left, right, res = [1] * size, [1] * size, []
        
    for i in range(1, size):
        left[i] = left[i-1] * nums[i-1]
            
    for i in range(size-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
            
    for i in range(size):
        res.append(left[i]*right[i])
            
    return res