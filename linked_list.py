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
        