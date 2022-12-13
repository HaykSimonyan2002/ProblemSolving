class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        lst = [] # time: 1
        lst_ = [] # time: 1
        s = s.lower() # time: n
        for i in range(len(s)): # time: n 
            
            if 48 <= ord(s[i])<=57 or 65<=ord(s[i])<=90 or 97 <= ord(s[i])<=122: # time: 1
                lst.append(s[i]) # time: constant amortized
            
            
        for j in range(len(lst)):
            
            lst_.append(lst[-(j+1)]) # time: constant amortized
        #print(lst)
        #print(lst_)
        if lst == lst_: # time: O(1)
            
            return True # time: O(1)
        else: return False # time: O(1)
