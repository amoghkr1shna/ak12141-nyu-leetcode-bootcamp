# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        #init both slow and fast to the very first node

        while fast and fast.next:
            # in case the list length is odd, fast would point to none
            # in case the list length is even, fast.next would point to none
            fast = fast.next.next
            slow = slow.next

        node = None
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp
            #reversing the second half of the list

        first, second = head,node

        while second:
            if second.val!=first.val:
                return False
            
            first = first.next
            second = second.next
        return True

        