"""Leetcode 387
Given a string s, find the first non-repeating 
character in it and return its index. 
If it does not exist, return -1.
"""
class Solution:
    def firstUniqChar(self, s):
        lst = [] 
        
        for i in range(len(s)): # O(n)
            if s[i] not in lst: # O(1)
              if s[i] not in s[i+1:]: # O(1)
                return i # O(1)
              else: 
                lst.append(s[i]) # Amortise O(1)
        return -1 # O(1)
