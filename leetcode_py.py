import heapq

def kClosest(points, K): 
    heap = []
    for (x, y) in points:
        dis = (x * x + y * y) * -1
        if len(heap) == K:
            heapq.heappushpop(heap, (dis, x, y))
        else:
            heapq.heappush(heap, (dis, x, y))
    return [(x, y) for (dis, x, y) in heap]

def winSum(nums, K):
    if not nums or K == 0: 
        return []
    
    initial_sum = 0
    for i in range(K):
        initial_sum += nums[i]
    
    start, last = 0, K
    res = [initial_sum]
    while last < len(nums): 
        initial_sum = initial_sum + nums[last] - nums[start]
        res.append(initial_sum)
        last += 1
        start += 1
    
    return res

def longestPalindrome(s):
    ss = set()

    for char in s: 
        if char in ss: 
            ss.remove(char)
        else:
            ss.add(char)
    
    if len(ss) == 0:
        return len(s)
    else: 
        return len(s) - len(ss) + 1


