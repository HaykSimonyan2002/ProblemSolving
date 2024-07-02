class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = -1

        if m == 0:
                for i in range(n):
                    nums1[i] = nums2[i] 
        else:
            while n >= 1:
                

                if nums1[m-1] < nums2[n-1]:
                    nums1[p1] = nums2[n-1]
                    n -= 1
                else:
                    nums1[p1] = nums1[m-1]
                    if m-2 >= 0:
                        m -= 1
                    else:
                        nums1[m-1] = nums2[n-1]
                        n-=1
                    
                p1 -= 1
