# Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

# Two pointer approach is used here where one pointer (fast) moves twice as fast as the other (slow). When the fast pointer reaches the end of the list, the slow pointer will be at the middle.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        