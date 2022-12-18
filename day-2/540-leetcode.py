# You are given a sorted array consisting of only integers where 
# every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) > 3:

            
            if mid%2==0:
                if nums[:mid][-1] == nums[:mid][-2]:
                    if mid/2 >= 1:
                        return self.singleNonDuplicate(nums[mid:])
                    else:
                        print("-----", nums[mid:][0], '----') 
                        return nums[mid:][0]
                elif nums[:mid][-1] == nums[mid:][0]:
                    if mid/2 >= 1:
                        return self.singleNonDuplicate(nums[:mid])
                else: 
                    print("-----", nums[:mid][-1], '----') 
                    return nums[:mid][-1]#self.singleNonDuplicate(nums[mid:])
            
            
            else:
                if nums[:mid][-1] == nums[:mid][-2]:
                    if mid/2>=1:
                        return self.singleNonDuplicate(nums[:mid])
                    else:
                        print("-----", nums[:mid][0], '----') 
                        return nums[:mid][0]
                elif nums[:mid][-1] == nums[mid:][0]:
                    if mid/2 >= 1:
                        return self.singleNonDuplicate(nums[mid:])
                else: return self.singleNonDuplicate(nums[:mid])
        
        
        elif len(nums) == 1:
            return nums[0]
        
        
        else:
            if nums[0] == nums[1]: return nums[-1]
            else: return nums[0]

            
