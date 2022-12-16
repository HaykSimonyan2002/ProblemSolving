# Given the head of a linked list and an integer val, 
# remove all the nodes of the linked list 
# that has Node.val == val, and return the new head.




class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        curr = head 
        prev = head
        while curr:
            if not prev.next:
                break
            if not head.next and head==val:
                return None
            elif prev.next.val == val:
                curr = curr.next
                prev.next = prev.next.next
            elif (prev.next.val != val) and (curr.next):
                prev = prev.next
                curr = curr.next
        if head:
            if head.val == val:
                if head.next:
                    head = head.next
                else: return None
        return head
