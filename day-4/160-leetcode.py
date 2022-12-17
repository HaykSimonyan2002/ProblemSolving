#Given the heads of two singly linked-lists headA and headB, 
#return the node at which the two lists intersect. 
#If the two linked lists have no intersection at all, return null.





# Bad time complextiy

# First version

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
            


            itemA = headA
            itemB = headB
                    
            
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
                        
                        
                        
                        
                        
# Second version



class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if (headA and headB):
            countA = countB = 1
            itemA = headA
            itemB = headB

            while itemA.next:
                countA += 1
                itemA = itemA.next
            print("countA ", countA)
            while itemB.next:
                countB += 1
                itemB = itemB.next
            print("countB ", countB)
            
            if itemA.val != itemB.val:
                print("itemA.val != itemB.val")
                return None

            
            itemA = headA
            itemB = headB
            print("itemA ", itemA)
            print("itemB ", itemB)




            if countA > countB:
                delta = countA - countB
                print("delta ",delta)
                print()
                print()
                while delta != 0:
                    print("itemA ", itemA)
                    print("delta ",delta)
                    itemA = itemA.next
                    delta -= 1
                print('----')
                print("itemA ", itemA)

            elif countA < countB:
                delta = countB - countA 
                print("delta ", delta)
                while delta != 0:
                    itemB = itemB.next
                    delta -= 1
                print("itemB ", itemB)




            while not(itemA == itemB):
                itemA = itemA.next
                itemB = itemB.next
            return itemA
