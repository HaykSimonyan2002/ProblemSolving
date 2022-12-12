class Solution:
    def secondfunc(self, list_1, list_2):
        item = 0
        for i in list_1:
          if i not in list_2:
            item = i
          else: continue
        return item
    def singleNumber(self, nums):
        lst_1=[]
        lst_2=[]
        if 1<= len(nums) <= 30000:
            for i in nums:
                if -30000 <= i <= 30000:
                    if i not in lst_1:
                        lst_1.append(i)
                    else: lst_2.append(i)
        return self.secondfunc(lst_1, lst_2)
    
