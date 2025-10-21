# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        #we're adding all elements in the stack
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        
        # if the list is 1,2,3,4
        # when we pop everything and link it we get
        # 1->4->3->2->None
        node = head
        while node:
            next_node = node.next
            end_node = stack.pop()

            if node == end_node or next_node == end_node:
                end_node.next = None
                break
            
            node.next = end_node
            end_node.next = next_node
            node = next_node
