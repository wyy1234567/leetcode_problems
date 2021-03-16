class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        preva = None 
        curra, currb = list1, list1 
        
        index = 0
        while index < a and curra:
            preva = curra 
            curra = curra.next
            index += 1 
            
        index = 0 
        while index < b and currb:
            currb = currb.next
            index += 1 
            
        next_node = currb.next
        currb.next = None
        preva.next = list2 
        
        curr = list2 
        while curr.next:
            curr = curr.next
        curr.next = next_node 
        
        return list1
    
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        # find the mid point
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half in-place
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next

        # Merge in-place; Note : the last node of "first" and "second" are the same
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return 