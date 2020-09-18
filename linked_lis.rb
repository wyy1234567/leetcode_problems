
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