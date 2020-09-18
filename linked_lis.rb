
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