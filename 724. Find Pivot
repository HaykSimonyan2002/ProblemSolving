class Solution:
    def pivotIndex(self, nums):
        if 1<= len(nums) <= 100000:
            for i in range(len(nums)): 
                if i == 0 and sum(nums[1:]) == 0:
                    return 0
                if 1<=i<(len(nums)-1) and sum(nums[:i]) == sum(nums[i+1:]):
                    return i
                elif i == (len(nums)-1) and sum(nums[:-1]) == 0:
                    return len(nums)-1
            return -1
