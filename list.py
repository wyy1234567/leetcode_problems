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