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

        


                    