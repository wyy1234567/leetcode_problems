import heapq
import math

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

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        curr = head
        while curr: 
            new_node = Node(curr.val)
            next_node = curr.next
            curr.next = new_node
            new_node.next = next_node
            curr = next_node
        
        curr = head
        while curr:
            if not curr.random:
                curr.next.random = None
            else: 
                curr.next.random = curr.random.next
            
            curr = curr.next.next
        
        curr = head.next
        while curr: 
            curr.next = curr.next.next
            curr = curr.next

        return head.next

# Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.
# Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.
# Example 1:
# Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation: 
# The average of the student with id = 1 is 87.
# The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

def highFive(slist):
    shash = {}
    for (x, y) in slist:
        if x not in shash:
            shash[x] = [y] #value is a heap: [sum, avg]
        else:
            if len(shash[x]) == 5:
                heapq.heappushpop(shash[x], y)
            else:
                heapq.heappush(shash[x], y)

    print(shash)
    res = []
    for k in shash:
        avg = math.floor(sum(shash[k]) / len(shash[k]))
        res.append([k, avg])
    return res
