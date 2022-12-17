# Given the head of a singly linked list, 
# reverse the list, and return the reversed list.


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            item = head
            temp = head
            item = temp.next
            temp.next = None

            while item and temp:
                #item = temp.next
                temp = item.next
                item.next = head
                head = item
                item = temp

            return head
