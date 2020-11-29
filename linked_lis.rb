
# Reverse a singly linked list.
# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

def reverse_list(head)
    return nil if !head
    prev = nil
    curr = head
    while curr do 
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    end
    prev
end

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# Example:
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5

def reverse_k_group(head, k)
    dummy = ListNode.new
    dummy.next = head
    prev = dummy
    while prev do 
        prev = reverse_nodes(prev, k)
    end
    dummy.next
end

#n1 -> n2 -> ... -> nk -> nk + 1
#nk -> nk-1 ->...-> n1 -> nk + 1
def reverse_nodes(prev, k)
    return nil if k <= 0 || !prev
    node1 = prev.next
    nodek = prev
    for i in 0...k do 
        return nil if !nodek
        nodek = nodek.next
    end
    return nil if !nodek
    nodekplus = nodek.next
    reverse(prev, prev.next, k)
    node1.next = nodekplus
    prev.next = nodek
    return node1
end

def reverse(prev, curr, k)
    for i in 0...k do 
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    end
end


# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list.

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

class Node
    attr_accessor :val, :next, :random
    def initialize(val = 0)
        @val = val
		  @next = nil
		  @random = nil
    end

    def copyRandomList(head)
        return nil if !head
        dummy = Node.new(0)
        dummy.next = head
        curr = head
    
        while curr do 
            new_node = Node.new(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next
        end
        curr = head
    
        while curr do 
            curr.next.random = curr.random.next if curr.random
            curr = curr.next.next
        end
    
        prev = dummy
        curr = head
        
        while curr do 
            copy = curr.next
            curr.next = copy.next
            prev.next = copy
            prev = copy
            curr = curr.next
        end
    
        dummy.next
    end
end

# Given the head of a linked list, return the list after sorting it in ascending order.
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end

    def sort_list(head)
        return head if !head || !head.next
        fast = head
        slow = head

        while fast.next && fast.next.next do 
            fast = fast.next.next
            slow = slow.next
        end

        mid = slow.next
        slow.next = nil
        
        left = sort_list(head)
        right = sort_list(mid)
        merge(left, right)
    end

    def merge(left, right)
        return left if !right
        return right if !left

        if left.val < right.val 
            head = left
            left = left.next
        else
            head = right
            right = right.next
        end

        curr = head

        while left && right do 
            if left.val < right.val 
                curr.next = left
                left = left.next
                curr = curr.next
            else
                curr.next = right
                right = right.next
                curr = curr.next
            end
        end

        curr.next = right if right
        curr.next = left if left

        head
    end
end

def swap_pairs(head)
    prev = ListNode.new
    prev.next = head
    new_head = prev
    while (prev.next && prev.next.next) do
        curr = prev.next
        next_node = curr.next
        node = next_node.next
        prev.next = next_node
        next_node.next = curr
        curr.next = node
        prev = curr
    end
    new_head.next   
end


