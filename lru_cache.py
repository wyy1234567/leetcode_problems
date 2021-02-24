class ListNode:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.next = None 
        self.prev = None 

    #remove the ListNode itself from the doubly linked list
    def remove(self):
        self.prev.next = self.next 
        self.next.prev = self.prev 
        self.next = None 
        self.prev = None 
    
    #insert a ListNode after itself
    def insert(self, node):
        next_node = self.next
        self.next = node 
        node.prev = self
        node.next = next_node
        next_node.prev = node

class LRUList:

    def __init__(self, capacity):
        self.size = capacity
        self.mapping = {}
        self.head = ListNode(float('-inf'), float('-inf'))
        self.tail = ListNode(float('inf'), float('inf'))
        self.head.next = self.tail 
        self.tail.prev = self.head 
        self.current_size = 0 
    
    def get(self, key):
        if key not in self.mapping:
            return -1 
        
        node = self.mapping[key]
        node.remove()
        self.tail.prev.insert(node)
        self.mapping[key] = node 
        return node.val

    def put(self, key, value):
        new_node = None 
        if key in self.mapping:
            new_node = self.mapping[key]
            new_node.remove()
            new_node.val = value 
        else:
            new_node = ListNode(key, value)
            self.current_size += 1

        if self.current_size > self.size:
            removed = self.head.next
            removed.remove()
            del self.mapping[removed.key]
            self.current_size -= 1 
        
        self.tail.prev.insert(new_node)
        self.mapping[key] = new_node