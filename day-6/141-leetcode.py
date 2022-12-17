# Given head, the head of a linked list, 
# determine if the linked list has a cycle in it.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        item = head
        while item and item.next:
            if item.next.val == None:
                return True
            item.val = None
            item = item.next
        return False
