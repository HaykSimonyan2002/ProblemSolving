#Given the heads of two singly linked-lists headA and headB, 
#return the node at which the two lists intersect. 
#If the two linked lists have no intersection at all, return null.

# Bad time complextiy



class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if headA and headB:
            countA = 0
            countB = 0
            itemA = headA
            itemB = headB

            while itemA:
                countA +=1
                itemA = itemA.next
            print(countA)

            while itemB:
                countB +=1
                itemB = itemB.next  
            print(countB)
            
            # Ok


            itemA = headA
            itemB = headB
                    


            # Problem
            # !!!!!!
            
            if countA > countB:
                while countA > countB:
                    new = ListNode(None) 
                    new.next = itemB
                    itemB = new
                    countB += 1
                print(itemB)

            elif countA <  countB:
                while countA<countB:
                    new = ListNode(None)
                    new.next = itemA
                    itemA = new
                    countA += 1
                print(itemA)


            if countA == countB:
                while itemA:
                    if itemA == itemB:
                        print("!!!!")
                        return itemA
                    else:
                        itemA = itemA.next
                        itemB = itemB.next
