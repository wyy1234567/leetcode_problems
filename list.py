class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
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
            

        


                    