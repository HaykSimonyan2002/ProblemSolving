#time complexity: O(n^2)!?!?!?

from math import prod
class Solution:

    def productExceptSelf(self, nums):
        answer = []
        lst = []
        
        for i in range(len(nums)):
            lst = nums.copy()
            lst.pop(i)
            answer.append(prod(lst))
        return answer


a = Solution()
a.productExceptSelf([-1,1,0,-3,3])


