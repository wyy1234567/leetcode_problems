import collections
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.random = None


    def mergeKList(self, lists): 
        if not lists:
            return None 
        
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2 
        left, right = self.mergeKList(lists[:mid]), self.mergeKList(lists[mid:])

        return self.mergeLists(left, right)
    
    def mergeLists(self, l1, l2):
        if not l1:
            return l2 
        if not l2:
            return l1 
        
        dummy = ListNode()
        curr = dummy 

        while l1 and l2: 
            if l1.val < l2.val:
                curr.next = l1 
                l1 = l1.next 
            else:
                curr.next = l2
                l2 = l2.next
        
            curr = curr.next 
        
        if l1:
            curr.next = l1
        
        if l2: 
            curr.next = l2 
        
        return dummy.next
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
            
        newHead = ListNode(0, None)
        curr = ListNode(0, None)
        newHead.next = curr
        carry = 0
            
        while l1 or l2: 
            curr_sum = carry
            if l1:
                curr_sum += l1.val
                l1 = l1.next
            if l2:
                curr_sum += l2.val
                l2 = l2.next
                
            curr.val = curr_sum % 10
            carry = curr_sum // 10
                
            if l1 or l2:
                curr.next = ListNode(0, None)
                curr = curr.next
            
        if carry != 0:
            curr.next = ListNode(carry, None)
        return newHead.next

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while curr.next:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        curr.next = prev
        return curr

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            

    
    def reverseList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

    def copyRandomList(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return None
        curr = head
        while curr:
            new_curr = ListNode(curr.val)
            next_node = curr.next
            curr.next = new_curr
            new_curr.next = next_node
            curr = next_node
        
        curr = head
        while curr:
            if not curr.random:
                curr.next.random = None
            else:
                curr.next.random = curr.random.next
            
            curr = curr.next.next
        curr = head.next
        while curr.next:
            next_node = curr.next.next
            curr.next = next_node
            curr = next_node
        
        return head.next
    
    def detectCycle(self, head):
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            # if there is an exception, we reach the end and there is no cycle
            return None

        # since fast starts at head.next, we need to move slow one step forward
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next

        return head

    def splitListToParts(self, root, k):
        cur = root 
        #Use loop to find length of linked list 
        for N in range(1001): 
            if not cur: break 
            cur = cur.next
        #Width = how many pieces to split into 
        #Remainder = make initial pieces larger than latter ones 
        width, remainder = divmod(N,k) #(a // b (floor), x % y)
        
        #Initialize solution to have right # of pieces 
        ans = [None for i in range(k)]
        
        pre = None 
        cur = root 
        for x in range(k):
            #start each piece with what's left
            ans[x] = cur
            #select how many pieces to put in box 
            for j in range(width + (1 if remainder > 0 else 0)): 
                pre = cur
                if cur: 
                    cur = cur.next
            if pre: 
                pre.next = None 
            remainder -= 1
            print (ans[x])
        return ans
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not n: return head
        l=[]
        while head:
            l+=[head.val]
            head=head.next
        del l[-n]
        l.reverse()
        t=None
        for elt in l:
            t= ListNode(elt,t)
        return t
    
    def deleteDuplicates(self, head):
        dic = {}
        node = head
        while node:
            dic[node.val] = dic.get(node.val, 0) + 1
            node = node.next
        node = head
        while node:
            tmp = node
            for _ in range(dic[node.val]):
                tmp = tmp.next
            node.next = tmp
            node = node.next
        return head


    def rotateList(self, head, k):
        if not head:
            return None 
        
        lastNode = head
        length = 1 
        
        while lastNode.next:
            lastNode = lastNode.next
            length += 1 
        
        k = k % length
        
        lastNode.next = head
        
        temp = head
        for _ in range(length - k - 1):
            temp = temp.next
        
        result = temp.next
        temp.next = None
        
        return result
    
    #place nodes that hold value less than x before, put remaining nodes after
    def partitionWithValue(self, head, x):
        before = beforeHead = ListNode(0)
        after = afterHead = ListNode(0)

        while head:
            if head.val < x:
                before.next = head 
                before = before.next 
            else:
                after.next = head
                after = after.next
            head = head.next 
        
        after.next = None 
        before.next = afterHead.next 
        return beforeHead.next



def merge(self, intervals):
        # intervals.sort(key = lambda l:l[0])
        intervals.sort()
        result = []
        for i in intervals: 
            #case 1: not overlap 
            if not result or i[0] > result[-1][1]: 
                result.append(i)
            #case 2: overlap exist 
            else: 
                result[-1][1] = max(i[1], result[-1][1])
        return result

def nextPermutation(nums):
        if not nums or len(nums) == 1:
            return 
        
        pointer = len(nums) - 2
        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1
            
        if pointer < 0:
            nums.sort() 
            return 
        
        min_gap = float('inf')
        index = 0
        for i in range(pointer + 1, len(nums)):
            if nums[i] > nums[pointer]:
                if nums[i] - nums[pointer] < min_gap:
                    min_gap = nums[i] - nums[pointer]
                    index = i
        
        temp = nums[pointer]
        nums[pointer] = nums[index]
        nums[index] = temp
        nums[(pointer+1):] = sorted(nums[(pointer+1):])
    

    
def searchInsert(nums, target):
        left, right = 0, len(nums)
        
        while left + 1 < right: 
            mid = left + (right - left) // 2 
            if nums[mid] == target: 
                return mid 
            
            if nums[mid] < target: 
                left = mid 
            else:
                right = mid 
                
        if nums[left] >= target:
            return left 
        
        return right


def findMaxElement(nums):
    left = 0 
    right = len(nums) - 1
        
    while left + 1 < right:
        mid = left + (right - left) // 2 
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid 
        elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
            left = mid 
        else:
            right = mid 
        
    if nums[left] > nums[right]:
        return left
    return right

def searchMatrix(matrix, target):
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        i, j = 0, n - 1 
        
        while i < m and j >= 0:
            num = matrix[i][j]
            if num == target:
                return True 
            elif num < target:
                i += 1
            else:
                j -= 1
        
        return False

def findMin(nums):
    last = nums[-1]
    left = 0
    right = len(nums) - 1 
    while left + 1 < right:
        mid = left + (right - left) // 2 
            
        if nums[mid] > last:
            left = mid 
        else:
            right = mid
        
    return min(nums[left], nums[right])


def subarraySum(nums, k):
    count, sum, numDic = 0, 0, {}
    numDic[0] = 1
        
    for i in range(len(nums)):
        sum += nums[i]
        toFind = sum - k
        if toFind in numDic:
            count += numDic[toFind]
        if sum in numDic:
            numDic[sum] += 1
        else:
            numDic[sum] = 1
        
    return count


def rotateMatrix(matrix):
    n = len(matrix)
        
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            temp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = temp


def canJump(nums):
    lastPosition = len(nums) - 1
        
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= lastPosition:
            lastPosition = i
                
    return lastPosition == 0

def lengthOfLastWord(self, s: str) -> int:
    arr = s.split()
        
    if arr:
        return len(arr[-1])
    else:
        return 0


def generateMatrix(self, n):
    matrix = [[0]*n for _ in range(n)]
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    d = 0
    y, x = 0, 0
    for i in range(1, n*n+1):
        matrix[y][x] = i
        dy, dx = directions[d % 4]
        if -1 < y+dy < n and -1 < x+dx < n and matrix[y+dy][x+dx] == 0:
            y, x = y+dy, x+dx
        else:
            d += 1
            dy, dx = directions[d % 4]
            y, x = y+dy, x+dx
    return matrix


def setZeroes(self, matrix):
    m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])

    for i in range(1, m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[0][j] = matrix[i][0] = 0

    for i in range(1, m):
        for j in range(n - 1, -1, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if firstRowHasZero:
        matrix[0] = [0] * n

def sortColors(nums):
    red, white, blue = 0, 0, len(nums)-1
    
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1


def combine(n, k):
        ret = []
        dfs(list(range(1, n+1)), k, [], ret)
        return ret
    
def dfs(nums, k, path, ret):
    if len(path) == k:
        ret.append(path)
        return 
    for i in range(len(nums)):
        dfs(nums[i+1:], k, path+[nums[i]], ret)

def findMinRotated(nums):
    pivot = nums[-1]
    left, right = 0, len(nums) - 1 

    while left + 1 < right:
        mid = left + (right - left) // 2

        if nums[mid] > pivot:
            left = mid
        else:
            right = mid
    
    if nums[left] <= pivot:
        return nums[left]
    else:
        return nums[right]

def findMinRotatedDuplicates(nums):

    pivot = nums[-1]
    left, right = 0, len(nums) - 1 

    while left + 1 < right:
        mid = left + (right - left) // 2

        if nums[mid] < pivot:
            right = mid 
        elif nums[mid] > pivot:
            left = mid 
        else:
            if nums[left] == nums[mid]:
                left += 1 
            else:
                right -= 1 
    return min(nums[left], nums[right])

def uniquePathsWithObstacles(obstacleGrid):
    col, row = len(obstacleGrid), len(obstacleGrid[0])

    if obstacleGrid[0][0] == 0:
        return 0 
    
    obstacleGrid[0][0] = 1 

    for i in range(1, col):
        obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
    
    for j in range(1, row):
        obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
    
    for i in range(1, col):
        for j in range(1, row): 

            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0
            else:
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

    return obstacleGrid[col-1][row-1]


def simplifyPath(path):

    stack = []

    for file in path.split('/'):
        if file in ('', '.'):
            pass
        elif file == '..':
            if stack:
                stack.pop()
        else:
            stack.append(file)

    return '/' + '/'.join(stack)


def combinations(n, k): 

    res = []

    def backtrack(n, k, res, path, index):
        if len(path) == k:
            res.append(path)
            return
        for i in range(index, n+1):
            backtrack(n, k, res, path+[i], i+1)
    
    backtrack(n, k, res, [], 1)
    return res

def removeDuplicatesSortedList(nums):
    index = 0 
    for n in nums:
        if index < 2 or n > nums[index - 2]:
            nums[index] = n 
            index += 1

    return index

def houseRobberI(nums):
    if not nums or len(nums) == 0:
        return 0
    
    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0]

    for i in range(2, len(dp)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
    
    return dp[-1]

def houseRobberII(nums):
    size = len(nums)

    notRobFront = [0] * (size + 1)
    notRobTail = [0] * (size + 1)

    notRobFront[1] = 0
    notRobTail[1] = nums[0]

    for i in range(2, size):
        notRobFront[i] = max(notRobFront[i-1], notRobFront[i-2]+nums[i-1])
        notRobTail[i] = max(notRobTail[i-1], notRobTail[i-2]+nums[i-1])
    
    notRobFront[-1] = max(notRobFront[size-1], notRobFront[size-2] + nums(-1))

    return max(notRobFront[-1], notRobTail[-2])


def wiggleMaxLength(nums):

    up, down = 1, 1 

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            up = down + 1
        if nums[i] < nums[i-1]:
            down = up + 1 
    
    return max(up, down)



def findRotateSteps(ring, key):
    index = collections.defaultdict(list)
    m, n = len(ring), len(key)
    dp = [[float('inf') for _ in range(m)] for _ in range(n)]

    #create a map to record index of every character in ring, only calculate these characters in keys 
    for i in range(m):
        index[ring[i]].append(i)
    
    #initialize the dp matrix with first character in key 
    for pos in index[key[0]]:
        dp[0][pos] = min(dp[0][pos], pos, m - pos)

    #start from the second character in key, calculate the path of moving it to 12'clock position
    for i in range(1, n):
        for curr in index[key[i]]:
            for pre in index[key[i-1]]:
                dp[i][curr] = min(dp[i][curr], dp[i-1][pre] + min(abs(curr - pre), m-abs(curr-pre)))
    
    ans = float('inf')
    for pos in index[key[-1]]:
        ans = min(ans, dp[n-1][pos])
    
    return ans + n

# Given an array nums of integers, you can perform operations on the array.
# In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.
# You start with 0 points. Return the maximum number of points you can earn by applying such operations. 
def deleteAndEarn(nums):
    freq = [0] * (max(nums) + 1)

    for n in nums:
        freq[n] += n 
    
    dp = [freq[0], max(freq[0], freq[1])]

    for i in range(2, len(freq)):
        dp.append(max(dp[i-1], freq[i]+dp[i-2]))
    
    return dp[-1]

# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
def checkRecord(n):
    dp00 = [0] * (n + 1)
    dp01 = [0] * (n + 1)
    dp02 = [0] * (n + 1)
    dp10 = [0] * (n + 1)
    dp11 = [0] * (n + 1)
    dp12 = [0] * (n + 1)

    dp00[0] = 1
    m = 10 ** 9 + 1

    for i in range(1, n+1):
        dp00[i] = dp00[i-1] + dp01[i-1] + dp02[i-1] #plus 3 P
        dp01[i] = dp00[i-1] #plus one L
        dp02[i] = dp01[i-1] #plus one L 
        dp10[i] = dp00[i-1] + dp01[i-1] + dp02[i-1] + dp10[i-1] + dp11[i-1] + dp12[i-1]
        dp11[i] = dp10[i-1]
        dp12[i] = dp11[i-1]
    
    return (dp00[n]+dp01[n]+dp02[n]+dp10[n]+dp11[n]+dp12[n]) % m

def maxProduct(nums):
    dpMax, dpMin = [0] * len(nums), [0] * len(nums)
    dpMax[0] = dpMin[0] = result = nums[0]

    for i in range(1, len(nums)):
        dpMax[i] = max(dpMax[i-1] * nums[i], dpMin[i-1]*nums[i], nums[i])
        dpMin[i] = min(dpMax[i-1] * nums[i], dpMin[i-1]*nums[i], nums[i])
        result = max(result, dpMax[i])
    
    return result

#Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                self.mark(i, 0, board)
            if board[i][n-1] == 'O':
                self.mark(i, n-1, board)
        
        for i in range(n):
            if board[0][i] == 'O':
                self.mark(0, i, board)
            if board[m-1][i] == 'O':
                self.mark(m-1, i, board)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
            
        
        
    
    def mark(self, i, j, board):
        m, n = len(board), len(board[0])
        queue= [[i, j]]
        x = [0,0,1,-1]
        y = [1,-1,0,0]
        
        while queue:
            curr = queue.pop() 
            currX = curr[0]
            currY = curr[1]
            board[currX][currY] = '#'
            
            for i in range(4):
                adjX = currX + x[i]
                adjY = currY + y[i]
                
                if adjX >= 0 and adjX < m and adjY >= 0 and adjY < n and board[adjX][adjY] == 'O':
                    queue.append([adjX, adjY])
    
    def largestDivisibleSubset(self, nums):   
        nums.sort()
        pre = [0] * len(nums)
        dp = [0] * len(nums)
        size, index, res = 0, -1, []
        
        for i in range(len(nums)):
            pre[i] = -1 
            dp[i] = 1 
            
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < 1 + dp[j]:
                    dp[i] = dp[j] + 1 
                    pre[i] = j 
            
            if size <= dp[i]:
                size = dp[i]
                index = i
                
        for i in range(size):
            res.append(nums[index])
            index = pre[index]
        
        return res
   
    def knapsack(self, values, weights, maxWeightConstraint):
        self.res = 0
    
        def backtrack(values, weights, maxWeightConstraint, currWeight, currVal):
            if currWeight > maxWeightConstraint:
                return 
            else:
                self.res = max(self.res, currVal)
            
            for i in range(len(weights)):
                backtrack(values[i+1:], weights[i+1:], maxWeightConstraint, currWeight+weights[i], currVal+values[i])
        
        backtrack(values, weights, maxWeightConstraint, 0, 0)
        return self.res

#find isolated city number 
def findCircleNum(isConnected):
    if not isConnected or not isConnected[0]:
        return 0 

    seen = [False] * len(isConnected)
    result = 0

    def findLinkedCity(isConnected, seen, curr):
        if seen[curr]:
            return 
        seen[curr] = True 

        for i in range(len(isConnected)):
            if not seen[i] and isConnected[curr][i] == 1:
                findLinkedCity(isConnected, seen, i) 
    
    for i in range(len(isConnected)):
        if not seen[i]:
            result += 1 
            findLinkedCity(isConnected, seen, i) 
    
    return result

def maxSlidingWindow(nums, k):
    result, arr = [], []

    for index, num in enumerate(nums):

        while arr and nums[arr[-1]] < num:
            arr.pop()
        
        arr.append(index)

        if arr[0] == index - k:
            arr.pop(0) 
        
        if index >= k - 1:
            result.append(nums[arr[0]])

    return result

def minSlidingWindow(nums, k):
    result, arr = [], []

    for index, num in enumerate(nums):

        while arr and nums[arr[-1]] > num:
            arr.pop()
        
        arr.append(index)

        if arr[0] == index - k:
            arr.pop(0) 
        
        if index >= k - 1:
            result.append(nums[arr[0]])

    return result

import collections
def findOrder(numCourses, prerequisites): 
    result = []
    #store {course: number of prerequisites}
    course_number_needed = collections.defaultdict(int)

    #sotre {prerequisite:course}
    pre_to_course = collections.defaultdict(set)

    for c in prerequisites:
        course_number_needed[c[0]] += 1 
        pre_to_course[c[1]].add(c[0])

    queue = []
    seen = [False] * numCourses
    for num in range(numCourses):
        if num not in course_number_needed:
            queue.append(num)
    
    while queue:
        current = queue.pop(0)
        seen[current] = True 
        result.append(current)

        for course in pre_to_course[current]:
            course_number_needed[course] -= 1 

            if course_number_needed[course] == 0 and not seen[course]:
                queue.append(course)
    
    for i in seen:
        if not i:
            return []

    return result

def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visit = [0 for _ in range(numCourses)]
    for x, y in prerequisites:
        graph[x].append(y)
        
    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True
    
def maxPoints(points):
    result = 0
    for i in range(len(points)):
        dic = {'cur':1}
        same = 0 
        for j in range(i+1, len(points)):
            x, y = points[j][0], points[j][1]
            slope = None
            if x == points[i][0] and y == points[i][1]:
                same += 1
                continue 
            if x == points[i][0]:
                slope = 'curr'
            else:
                slope = (points[i][1]-y) * 1.0 /(points[i][0]-x)
            if slope not in dic:
                dic[slope] = 1 
            dic[slope] += 1
        result = max(result, max(dic.values())+same)
    return result


def maximalNetworkRank(n, roads):
    road_dict = set()
    freq = [[] for _ in range(n)]
    road_count = collections.defaultdict(int)
    
    for road in roads:
        road_count[road[0]] += 1 
        road_count[road[1]] += 1 
        road_dict.add((road[0], road[1]))
        
    for k, v in road_count.items():
        freq[v].append(k)
        
    candidates = []
    index, count = n-1, 0 
    
    while index >= 0 and count < 2:
        if len(freq[index]) > 1 and count == 0:
            candidates = freq[index]
            break 
        if freq[index]:
            for r in freq[index]:
                candidates.append(r)
            count += 1 
        index -= 1
        
    res = 0

    for i in range(len(candidates)):
        for j in range(i+1, len(candidates)):
            count = road_count[candidates[i]] + road_count[candidates[j]]
            if (candidates[i], candidates[j]) in road_dict or (candidates[j], candidates[i]) in road_dict:
                count -= 1
            res = max(res, count)
            
    return res


def orangesRotting(grid):
    queue = []
    result = 0
    rows, cols = len(grid), len(grid[0])
    r_dir, c_dir = [1,-1,0,0], [0,0,1,-1]
    seen = [[False for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append([i, j])
            if grid[i][j] == 0:
                seen[i][j] = True
    
    while queue:
        size = len(queue)
        result += 1 
        
        for _ in range(size):
            current = queue.pop(0)
            r, c = current[0], current[1]
            seen[r][c] = True 
            
            for i in range(4):
                nr = r + r_dir[i]
                nc = c + c_dir[i]
                
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and not seen[nr][nc] and grid[nr][nc] == 1:
                    queue.append([nr, nc])
                    grid[nr][nc] = 2
    
    for i in range(rows):
        for j in range(cols):
            if not seen[i][j]:
                return -1 
    
    if result != 0:
        return result - 1 
    else:
        return 0

# Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
def consecutiveNumbersSum(N):
    i, ans = 1, 0
    while N > i * (i - 1) // 2:
        if (N - i * (i - 1) // 2) % i == 0:
            ans += 1
        i += 1
    return ans


def maxAreaOfIsland(grid):
    seen = set()
    def area(r, c):
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                and (r, c) not in seen and grid[r][c]):
            return 0
        seen.add((r,c))
        return (1 + area(r+1, c) + area(r-1, c) +
                area(r, c-1) + area(r, c+1))
    
    return max(area(r,c) for r in range(len(grid)) for c in range(len(grid[0])))