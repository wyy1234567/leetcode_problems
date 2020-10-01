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

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    
    def findSubtree(self, root):
        self.max_sum = float('-inf')
        self.max_node = None

        def nodeSum(root): 
            if not root:
                return 0
            
            left_sum = nodeSum(root.left)
            right_sum = nodeSum(root.right)
            curr = root.val + left_sum + right_sum
            if curr > self.max_sum:
                self.max_sum = curr
                self.max_node = root
            return curr
        
        nodeSum(root)
        return self.max_node

def validWordAbbreviation(self, word, abbr):
        if not word or not abbr or abbr[0] == '0':
            return False
        
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + (ord(abbr[j]) - ord('0'))
                    j += 1 
                i += num 
            else:
                if abbr[j] == word[i]:
                    i += 1 
                    j += 1 
                else:
                    return False 
            
        if i == len(word) and j == len(abbr):
            return True
        else: 
            return False

class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        self.ans = []
        
        def addRange(low, high):
            if low > high:
                return
            if low == high:
                self.ans.append(str(low))
                return 
            string = str(low) + '->' + str(high)
            self.ans.append(string)
            
        if len(nums) == 0:
            addRange(lower, upper)
            return self.ans
        
        addRange(lower, nums[0] - 1)
        for i in range(1, len(nums)):
            addRange(nums[i - 1] + 1, nums[i] - 1)
        
        addRange(nums[len(nums) - 1] + 1, upper)
        return self.ans 

    
#valid num: 符号+浮点数+e+符号+整数，前后可以有空格
def isNumber(self, s: str) -> bool:
    i = 0
    s = s.strip() + ' '
    size = len(s) - 1

    if s[i] == '+' or s[i] == '-':
        i += 1
    
    point, num = 0, 0

    while s[i].isdigit() or s[i] == '.':
        if s[i].isdigit():
            num += 1
        if s[i] == '.':
            point += 1
        i += 1

    if point > 1 or num < 1:
        return False
    
    if s[i] == 'e':
        i += 1
        if s[i] == '+' or s[i] == '-':
            i += 1
        
        if i == size:
            return False 
        
        while i < size:
            if not s[i].isdigit():
                return False
            i += 1
    
    return i == size


